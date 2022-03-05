from flask import Flask, redirect, request, render_template, url_for
from datetime import datetime
from youtube_transcript_api import YouTubeTranscriptApi as ytapi
import getTranscript
from gtts import gTTS

# define a variable to hold you app
app = Flask(__name__)

# define your resource endpoints
@app.route('/')
def index_page():
    return "Hello world"

@app.route('/time', methods=['GET'])
def get_time():
    return str(datetime.now())

@app.route('/player')
def audio_render():
    return render_template('player.html')

@app.route('/<path:subpath>')
def show_subpath(subpath):
    # get the video ID
    videoId = request.args.get('v') 
    transcript = ytapi.get_transcript(videoId)
    trans = getTranscript.getTrans(transcript)
    tts = gTTS(trans)
    # save the audio in audio folder
    tts.save('audio/transcript.mp3')
    return redirect(url_for('audio_render'))

# server the app when this file is run
if __name__ == '__main__':
    app.run(debug=True)

# temp change
