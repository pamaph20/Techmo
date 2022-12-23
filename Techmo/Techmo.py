import requests 
import json
import os
import openai
import os
import time
import playsound
import config
import speech_recognition as sr
from gtts import gTTS



def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said
def say(text):
    response = requests.post(
        'https://api.openai.com/v1/completions',
        headers = {'Content-Type' : 'application/json','Authorization' : 'Bearer %s' % (config.api_token,)},
        json = {"model" : "text-davinci-003", "prompt" : text, "max_tokens" : 2040, "temperature":1.5})
    #requests.post("example-url", headers={"Content-Type": "application/json", "Authorization": f"Bearer {token}"}, data={"the": "data"})
    data = response.json()
    speak(data["choices"][0]["text"])

text = get_audio()
say(text)








