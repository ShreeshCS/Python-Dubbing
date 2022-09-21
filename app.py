from googletrans import *
from flask import *
from youtube_transcript_api import YouTubeTranscriptApi as ytapi
import getTranscript
from gtts import gTTS
import urllib.request
import json
import urllib
import pprint

# pip install googletrans==3.1.0a0

# define a variable to hold you app
app = Flask(__name__)

# defining resource endpoints
@app.route('/', methods = ['GET'])
def index():
    return render_template('home.html')


@app.route('/convert', methods = ['GET', 'POST'])
def get_url():
    # Get the full valid URL
    link = (request.form.get('link'))
    
    
    # # Get Video Title To display in Player page
    # with urllib.request.urlopen(link) as response:
    #     response_text = response.read()
    #     data = json.loads(response_text.decode())
    #     video_title = data['title']


    # get the video ID
    videoId = ""
    for i in range(len(link)):
        if link[i] == 'v':
            videoId = link[i+2::]
            break
    lang = request.form.get('language')

    translator = Translator()
    
    json_trans = ytapi.get_transcript(videoId , languages=['en'])
    trans = getTranscript.getTrans(json_trans)
    if(lang == 'hindi'):
        language = 'hi'
        translated_transcript = translator.translate(text=trans , dest='hi' , src="auto")
    else:
        language = 'en'
        translated_transcript = translator.translate(text=trans , dest='en' , src="auto")
    # print(translated_transcript)
    tts = gTTS(text=translated_transcript.text , lang=language)
    print(lang)
    print(translated_transcript.text)
    # save the audio in audio folder
    tts.save('audio/transcript.mp3')
    return redirect(url_for("audio_render"))



@app.route('/convert/player', methods=['GET', 'POST'])
def audio_render():
    return render_template('index.html')

# FUNCTION THAT LETS YOU MAKE A DIRECTORY ACCESSIBLE TO THE PUBLIC
@app.route("/audio/<path:filename>")
def static_dir(filename):
    return send_from_directory("audio", filename)


# server the app when this file is run
if __name__ == '__main__':
    app.run(debug=True)


