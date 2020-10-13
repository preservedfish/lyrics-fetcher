import requests
import base64
from flask import request, session
from secret import client_id, client_secret


SCOPE = 'user-read-currently-playing'
REDIRECT_URI = 'http://localhost:5000/callback'


def get_song():
    while True:
        # If the access token exists
        if 'access_token' in session:
            access_token = session['access_token']
            
            # ---- GET SONG AND ARTIST NAMES ----
            headers = {'Content-Type' : 'application/json', 
                    'Authorization': 'Bearer ' + access_token}

            re = requests.get('https://api.spotify.com/v1/me/player/currently-playing', headers = headers)

            if re.status_code == 200: # Success
                song_name = re.json()['item']['name']
                artist_name = re.json()['item']['album']['artists'][0]['name']
                return (song_name, artist_name)
            elif re.status_code == 401:
                refresh_token = session['refresh_token']

                # ---- USE REFRESH TOKEN ----
                client_id64 = base64.b64encode(client_id)
                client_secret64 = base64.b64encode(client_secret)
                ref_re = requests.post('https://accounts.spotify.com/api/token', {
                    'grant_type': 'refresh_token',
                    'refresh_token': refresh_token}, {
                    'Authorization': 'Basic' + f'{client_id64}:{client_secret64}'
                    })

                session['access_token'] = ref_re.json()['access_token']
            elif re.status_code == 204: # No song playing
                return ('Couldn\'t find your song. Are you listening to one?', 'If you\'re not listening to a song, can there be an artist?')
        # Get an access token
        else:
            # ---- GET AUTHORIZATION CODE----
            code = request.args.get('code')

            # ---- GET TOKENS ----
            token_re = requests.post('https://accounts.spotify.com/api/token', {
                'grant_type': 'authorization_code',
                'code': code,
                'redirect_uri': REDIRECT_URI,
                'client_id': client_id,
                'client_secret': client_secret,
                'scope': SCOPE   
                })

            session['access_token'] = token_re.json()['access_token']
            session['refresh_token'] = token_re.json()['refresh_token']
def get_url():
    return f'https://accounts.spotify.com/authorize?response_type=code&client_id={client_id}&scope={SCOPE}&redirect_uri={REDIRECT_URI}'