import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS

def speak(text):
    tts = gTTS(text=text,lang='pt-br')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio,language='pt-BR')
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
    return said

speak("Olá, como posso ajudar?")

text = get_audio()

if "como vai você" in text:
    speak("Estou bem, e você?")

if "seu nome" in text:
    speak("Meu nome é Jarvis")