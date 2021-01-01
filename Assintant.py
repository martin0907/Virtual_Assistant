import speech_recognition as sr
from datetime import date
from gtts import gTTS
import webbrowser
import wikipedia
import playsound
import pyaudio
import time

def speak(text):
    tts = gTTS(text=text, lang='en-us')
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def get_audio():
    r = sr.Recognizer()
    print("i am listening...")
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Execption" + str(e))

    return said

speak("How can I help you?")
text = get_audio()

if "open YouTube" in text:
    webbrowser.open('https://www.youtube.com')

if "I want to check my Gmails" in text:
    try:
        webbrowser.open("https://mail.google.com")
        webbrowser.open("https://mail.google.com")
    except Exception as error:
        print("Exception" + str(error))
        speak("I have no access to your Google accounts!")

if "how are you" in text:
    speak("I am fine thanks.")

if "how old are you" in text:
    speak("Well, I came into existence gradually.But my first day as an assistant was December 23, 2020.")

if "search for" in text:
    speak("I'm listening")
    webbrowser.open("https://www.google.sk/?#q=" + text)

if "about" in text:
    speak("I'm listening")
    text = get_audio()
    content = wikipedia.summary(text)
    speak(content)