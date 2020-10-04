import requests
import base64
from flask import request
from secret import client_id, client_secret


scope = 'user-read-currently-playing'
redirect_uri = 'http://localhost:5000/callback'


def get_song():
    # ---- GET AUTHORIZATION CODE----
    code = request.args.get('code')


    # ---- GET TOKENS ----
    token_re = requests.post('https://accounts.spotify.com/api/token', {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri,
        'client_id': client_id,
        'client_secret': client_secret,
        'scope': scope   
        })

    access_token = token_re.json()['access_token']
    refresh_token = token_re.json()['refresh_token']


    # ---- GET SONG AND ARTIST NAMES ----
    headers = {'Content-Type' : 'application/json', 
            'Authorization': 'Bearer ' + access_token}

    re = requests.get('https://api.spotify.com/v1/me/player/currently-playing', headers = headers)

    if re.status_code == 200: # Success
        song_name = re.json()['item']['name']
        artist_name = re.json()['item']['album']['artists'][0]['name']
        return (song_name, artist_name)
    elif re.status_code == 401:
        # ---- USE REFRESH TOKEN ----
        client_id64 = base64.b64encode(client_id)
        client_secret64 = base64.b64encode(client_secret)
        ref_re = requests.post('https://accounts.spotify.com/api/token', {
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token}, {
            'Authorization': 'Basic' + f'{client_id64}:{client_secret64}'
            })
        access_token = ref_re.json()['access_token']
    elif re.status_code == 204: # No song playing
        return ('Couldn\'t find your song. Are you listening to one?', 'If you\'re not listening to a song, can there be an artist?')

def get_url():
    return f'https://accounts.spotify.com/authorize?response_type=code&client_id={client_id}&scope={scope}&redirect_uri={redirect_uri}'