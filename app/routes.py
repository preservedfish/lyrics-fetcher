from flask import render_template
from app import app
import app.songs as songs
import app.lyrics as lyrics

@app.route('/')
@app.route('/index')
def index():
    url = songs.get_url()
    return render_template('index.html', title = 'Home', url = url)

@app.route('/callback')
def display_lyrics():
    result = songs.get_song()
    my_lyrics = lyrics.get_lyrics(result[0], result[1])
    return render_template('lyrics.html', title = 'Currently Playing', song_name = result[0], artist_name = result[1], lyrics = my_lyrics)