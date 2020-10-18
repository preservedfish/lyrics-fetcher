# A program for displaying song lyrics
![Login](./assets/login_page.PNG?raw=true)
![Lyrics](./assets/lyrics_page.PNG?raw=true)

Written in Python, deployed using Flask. Utilizes the Spotify API to fetch the song name and the Genius API to fetch the lyrics. Uses [Bootstrap](https://getbootstrap.com/) for the CSS.

Tested on Windows 10 and Python 3.7.

## Getting started
### Installing the modules
    pip install -r requirements.txt
The `requirements.txt` file contains the names of the modules needed. They can be installed using the above command.

### Running the program
    set FLASK_APP = lyrics_fetcher.py
    flask run
After changing the directory to the program folder, use these two commands to run the program itself. Then open your favorite browser and visit http://localhost:5000.

### Required accounts
First and foremost, you'll need a [Spotify](https://www.spotify.com/) account. This program will fetch the song you're currently playing in Spotify. I don't provide the credentials needed to access the API (client_id and client_secret), so you'll also need to [register an application](https://developer.spotify.com/dashboard/) with Spotify. This doesn't take long, but one thing you'll have to do is set a redirect URI. Set this to http://localhost:5000/callback.

Spotify will fetch the song name. To get the lyrics, you'll need a [Genius](https://genius.com/) account. Similarly, you'll also need to [register an app](http://genius.com/api-clients) with Genius. This step is simpler though, as unlike Spotify you'll be getting a client access token directly from Genius--meaning no client ids, client secrets, or redirect URIs for Genius.

Afterwards, you'll need to store these values (client_id, client_secret, access_token) in `secret.py`. Instructions can be found in there.

---
This was my first big project. First webapp and first time using APIs.

Writing this for posterity ~ September 2020.