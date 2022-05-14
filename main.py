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
            recon.adjust_for_ambient_noise(source)
            audio = recon.listen(source)
            command = recon.recognize_google(audio, language='pt')
            command = command.lower()
            return command
    except:
        pass


def aguardando_sexta_feira():
    with sr.Microphone() as source:
        try:
            while True:
                print("pode falar")
                audio = recon.listen(source)
                command = recon.recognize_google(audio, language='pt')
                command = command.lower()
                print(command)
                if command == "ok sexta-feira":
                    talk("Sim mestre. O que posso fazer")
                    main()
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
    if len(ler_arquivo()) == 0:
        arquivo = open('agenda.txt', 'w')
        arquivo.write(unidecode(compromisso, '\n'))
        arquivo.close()
        print("cadastrado")
    else:
        arquivo = open('agenda.txt', 'a')
        arquivo.write(unidecode(compromisso, '\n'))
        arquivo.close()
        print("incrementado")


def ler_arquivo():
    texto_para_falar = []
    arquivo = open('agenda.txt', 'r')
    for linha in arquivo:
        texto_para_falar.append(linha.strip())
    arquivo.close()
    return texto_para_falar


def main():
    try:
        while True:
            command = comando()
            print(command)
            if command in 'data':
                d1 = datetime.today().strftime('%d-%m-%Y')
                talk(d1)
                return
            elif command in 'cadastrar evento' or command == 'cadastrar evento':
                cadastrar_evento_na_agenda()
                return
            elif command in 'agenda' or command == 'ler agenda' or command == 'ver agenda':
                texto_para_falar = ler_arquivo()
                talk(texto_para_falar)
                return
            elif 'solteira' in command or command == 'você esta solteira':
                talk('Eu estou em um relacionamento com o wi-fi')
                return
            elif 'encontro' in command:
                talk('desculpe, estou com dor de cabeca')
                return
            else:
                talk("Não entendi, poderia repetir por favor")

    except:
        pass


while True:
    aguardando_sexta_feira()
