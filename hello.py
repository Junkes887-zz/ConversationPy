import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

def cria_audio(audio):
    tts = gTTS(audio,lang='pt-br', show=False)
 
    tts.save('audios/hello.mp3')
    print("Estou aprendendo o que você disse...")

    playsound('audios/hello.mp3')
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
frase = ouvir_microfone()
cria_audio("Teste")