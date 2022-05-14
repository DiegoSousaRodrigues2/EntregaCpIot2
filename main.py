import speech_recognition as sr
import pyttsx3
from datetime import datetime
from unidecode import unidecode

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
            while True:
                print("pode falar")
                audio = recon.listen(source)
                command = recon.recognize_google(audio, language='pt')
                command = command.lower()
                print(command)
                if command == "ok sexta-feira":
                    return True
    except:
        pass


def cadastrar_evento_na_agenda():
    try:
        with sr.Microphone() as source:
            talk("Okay pode me falar o que devo agendar")
            audio = recon.listen(source)
            command = recon.recognize_google(audio, language='pt')
            command = command.lower()
            cadastrar_aquivo(command)
    except:
        pass


def cadastrar_aquivo(compromisso):
    arquivo = open('agenda.txt', 'w')
    arquivo.write(unidecode(compromisso))
    arquivo.close()
    print("cadastrado")


def ler_arquivo():
    texto_para_falar = []
    arquivo = open('agenda.txt', 'r')
    for linha in arquivo:
        texto_para_falar.append(linha.strip())
    arquivo.close()
    talk(texto_para_falar)
    print("pomba")


def main():
    try:
        while not aguardando_sexta_feira():
            aguardando_sexta_feira()
        command = comando()
        print(command)
        if command in 'data':
            d1 = datetime.today().strftime('%d-%m-%Y')
            talk(d1)
        elif command in 'cadastrar evento' or command == 'cadastrar evento':
            cadastrar_evento_na_agenda()
        elif command in 'agenda' or command == 'ler agenda' or command == 'ver agenda':
            ler_arquivo()
        else:
            talk("Não entendi, poderia repetir por favor")

    except:
        pass


while True:
    main()
