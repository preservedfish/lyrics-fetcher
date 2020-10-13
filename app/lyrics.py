import requests
import bs4
from secret import access_token


def get_lyrics(song, artist):
    modified_song_name = song.replace(' ', '%20')

    # ---- GET LYRICS ----
    headers = {'Content-Type': 'application/json',
               'Authorization': 'Bearer ' + access_token}
    search_re = requests.get(f'https://api.genius.com/search?q={modified_song_name}', headers=headers)
    if search_re.status_code == 200:
        search_results = search_re.json()
        for song in search_results['response']['hits']:
            if artist == song['result']['primary_artist']['name']:
                lyrics_page = song['result']['url']
                soup = bs4.BeautifulSoup(requests.get(lyrics_page).text, 'html.parser')
                elems = soup.select('.song_body-lyrics')
                lyrics = elems[0].text.strip()
                return lyrics
