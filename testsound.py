# from gtts import gTTS
# import time
# from playsound import playsound
# import os
# import datetime
from flask import Flask, render_template, request,send_from_directory
app = Flask(__name__,template_folder='template')
totaltexts=[]
@app.route('/')
def index():
    return render_template('start.html',lis=totaltexts)
@app.route("/index",methods=['POST','GET'])
def convert():
    import pyttsx3
    text = ''
    import speech_recognition as sr
    r = sr.Recognizer()
    r.dynamic_energy_adjustment_ratio = 1
    try:
        with sr.Microphone() as source:
                print("Speak :")
                r.energy_threshold = 5500
                r.pause_threshold=1
                audio = r.adjust_for_ambient_noise(source)
                audio=r.listen(source,timeout=None,phrase_time_limit=3)
                #audio = r.record(source, duration=None)
                engine = pyttsx3.init()
                voices = engine.getProperty('voices')
                engine.setProperty('voice', voices[1].id)
                # try:
                text = r.recognize_google(audio)
                totaltexts.append(text)
                print("You said : {}".format(text))
        return  render_template('start.html',lis=totaltexts)
    except:
        print('No voice found')
        return render_template('start.html',lis=totaltexts)
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000)