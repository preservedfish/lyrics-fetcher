from decouple import config


"""Before you continue, please read README.md and make sure that you followed the steps for registering an app with Spotify and Genius.

There are two ways of entering the values correctly, an easy way and a hard way:
The hard way is to create a .env file and store the values in there.
    For example, for the Genius access token you'd enter GENIUS_ACCESS_TOKEN=ex@mple in the .env file.
(RECOMMENDED) The easy way is to replace the default values below with the corresponding values.
    For example, for the Genius access token you'd replace ex@ample with the actual token.
"""

"""Genius Client Access Token"""
access_token = config('GENIUS_ACCESS_TOKEN', default='ex@ample')

"""Spotify Client ID + Client Secret"""
client_id = config('SPOTIFY_CLIENT_ID', default='ex@ample')
client_secret = config('SPOTIFY_CLIENT_SECRET', default='ex@ample')
