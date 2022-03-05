from googletrans import Translator
from flask import *
from youtube_transcript_api import YouTubeTranscriptApi as ytapi
import getTranscript
from gtts import gTTS

# define a variable to hold you app
app = Flask(__name__)

# defining resource endpoints
@app.route('/', methods = ['GET'])
def index():
    return render_template('home.html')

@app.route('/converting/player', methods=['GET', 'POST'])
def audio_render():
    return render_template('player.html')

@app.route('/converting', methods = ['GET', 'POST'])
def get_url():
    # Get the full valid URL
    link = (request.form.get('link'))
    # get the video ID
    videoId = ""
    for i in range(len(link)):
        if link[i] == 'v':
            videoId = link[i+2::]
            break
    lang = request.form.get('language')

    if(lang == 'English'):
        language = 'en'
    else:
        language = 'hi'

    translator = Translator() 
    json_trans = ytapi.get_transcript(videoId)
    trans = getTranscript.getTrans(json_trans)
    # translated_transcript = translator.translate(trans, dest=(language))
    tts = gTTS(text=trans)
    # tts = gTTS(text=translated_transcript, lang=str(language))
    # save the audio in audio folder
    tts.save('templates/audio/transcript.wav')
    return redirect(url_for("audio_render"))



@app.route('/converting/<audio_file_name>', methods=['GET', 'POST'])
def returnAudioFile(audio_file_name):
    path_to_audio_file = "C:/Users/Lenovo/PycharmProjects/pythonDubbing/templates/audio/" + audio_file_name
    return send_file(
         path_to_audio_file, 
         mimetype="audio/mpeg", 
         as_attachment=True, 
         attachment_filename="transcript.wav")


   
# @app.route('/converting/<link>', methods = ['GET', 'POST'])
# def show_subpath(link):
#     # get the video ID
#     videoId = request.args.get('v') 
#     # videoLang = request.args.get('language')
#     # todo: add a language selector and convert transcript to custom language
#     transcript = ytapi.get_transcript(videoId)
#     trans = getTranscript.getTrans(transcript)
#     tts = gTTS(trans)
#     # save the audio in audio folder
#     tts.save('audio/transcript.mp3')
#     return redirect(url_for('audio_render'))

# server the app when this file is run
if __name__ == '__main__':
    app.run(debug=True)


