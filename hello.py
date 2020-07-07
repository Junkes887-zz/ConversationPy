import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

def cria_audio(audio):
    tts = gTTS(text=text,lang='pt-br')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
def ouvir_microfone():
    microfone = sr.Recognizer()

    with sr.Microphone() as source:
        audio = microfone.listen(source)
        frase = microfone.recognize_google(audio,language='pt-BR')
  
    try:
        print("Você disse: " + frase.capitalize())
        if frase.capitalize() == "Meu nome é eder":
            print("Viado Detectado")
    except sr.UnkownValueError:
        print("Não entendi")
    
    return frase

frase = ouvir_microfone()
cria_audio(frase)