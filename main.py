import speech_recognition as sr
import pyttsx3
from datetime import datetime

recon = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def comando():
    try:
        with sr.Microphone() as source:
            talk("Sim mestre. O que posso fazer")
            audio = recon.listen(source)
            command = recon.recognize_google(audio, language='pt')
            command = command.lower()
            return command
    except:
        pass


def aguardando_sexta_feira():
    try:
        with sr.Microphone() as source:
            command = ""
            while command != "ok sexta-feira":
                audio = recon.listen(source)
                command = recon.recognize_google(audio, language='pt')
                command = command.lower()
                return
    except:
        pass


def main():
    try:
        aguardando_sexta_feira()
        command = comando()
        if "data" in command:
            d1 = datetime.today().strftime('%d-%m-%Y')
            print(d1)
            talk(d1)
        else:
            talk("Não entendi, poderia repetir por favor")
    except:
        pass


main()

# def talk(text):
#     engine.say(text)
#     engine.runAndWait()
#
#
# def wait_command():
#     try:
#         with sr.Microphone() as source:
#             print('Fale algo')
#             audio = recon.listen(source)
#             command = command.lower()
#             if 'alexa' in command:
#                 command = command.replace('alexa', '')
#                 print(command)
#                 return command
#     except:
#         pass
#
# def run_sexta():
#     command = wait_command()
#     if command == 'sla':
#         engine.say('Teste')
#         engine.runAndWait()
#
# while True:
#     run_sexta()
