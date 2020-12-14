# A program for displaying song lyrics
![Login](./assets/login_page.PNG?raw=true)
![Lyrics](./assets/lyrics_page.PNG?raw=true)

Written in Python, deployed using Flask. Utilizes the Spotify API to fetch the song name and the Genius API to fetch the lyrics. Uses [Bootstrap](https://getbootstrap.com/) for the CSS. This program is also [Dockerized](https://www.docker.com/).

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

## Docker
You can also run this program in a container via [Docker](https://www.docker.com/). This will be a bit different from running the program the usual way. Notably, you won't need to have Python and the prerequisites installed beforehand; they'll be taken care of when the image is built. The instructions will assume that you have Docker installed and already took care of registering an app with Spotify and Genius.

### Building an image
    docker build -t lyrics_fetcher .
Building an image is simple. After checking that Docker is open and that your current directory is this program, run the above command. This will create an image called lyrics_fetcher with a size around 891MB. This image will include all the components needed to run the program.

### Running a container
    docker run -e GENIUS_ACCESS_TOKEN=t3st -e SPOTIFY_CLIENT_ID=t3st -e SPOTIFY_CLIENT_SECRET=t3st -p 5000:5000 lyrics_fetcher
Running a container is a bit more involved. You will enter the above command after the image has been created, but before you do that you will need to insert your Genius access token, Spotify client id, and Spotify client secret in the appropriate locations. `t3st` in the above command is a placeholder, so replace each instance of it with the appropriate value.

After the container is running, using the program is the same as before: just open http://localhost:5000 in a browser.

### Stopping the container
To stop the container, you can either enter the following in Command Prompt:

    docker stop <container_name>

...or stop it through the Docker Desktop client.

---
This was my first big project. First webapp and first time using APIs.

Writing this for posterity ~ September 2020.