import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
engine.say('Hello sir, how may I help you, sir.')
engine.runAndWait()

listener = sr.Recognizer()
