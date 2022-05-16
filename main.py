# https://github.com/DiegoSousaRodrigues2/EntregaCpIot2
import speech_recognition as sr
import pyttsx3
from datetime import datetime
from unidecode import unidecode
import random
import wikipedia

recon = sr.Recognizer()
engine = pyttsx3.init()
wikipedia.set_lang("pt")


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
                recon.adjust_for_ambient_noise(source, duration=0.3)
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
        talk("compromisso salvo")
    else:
        arquivo = open('agenda.txt', 'a')
        arquivo.write(unidecode(compromisso, '\n'))
        arquivo.close()
        talk("compromisso adicionado")


def ler_arquivo():
    texto_para_falar = []
    arquivo = open('agenda.txt', 'r')
    for linha in arquivo:
        texto_para_falar.append(linha.strip())
    arquivo.close()
    return texto_para_falar


def advinhe_o_numero():
    try:
        command = ""
        with sr.Microphone() as source:
            talk("Fale um numero de 1 a 10")
            audio = recon.listen(source)
            command = recon.recognize_google(audio, language='pt')
            command = command.lower()
            validar_numero(command)
    except:
        pass


def validar_numero(numero):
    try:
        numero = int(numero)
        if type(numero) == int and 0 < numero < 11:
            a = random.randint(0, 10)
            if numero == a:
                talk("Parabéns você acertou")
            else:
                talk("Sinto muito você errou")
    except:
        talk('Não foi informado um numero valido')


def pesquisar_wikipedia():
    try:
        command = ""
        with sr.Microphone() as source:
            talk("Me fale um topico para pesquisar")
            audio = recon.listen(source)
            command = recon.recognize_google(audio, language='pt')
            command = command.lower()
            if command != "":
                return command
    except:
        pass


def limpar_agenda():
    arquivo = open('agenda.txt', 'w')
    arquivo.write('')
    arquivo.close()
    talk('agenda limpa')


def listar_compromisso_dicionario():
    key = []
    linha_key = []
    for a in range(1, len(ler_arquivo()) + 1):
        key.append(a)
        linha_key.append('linha' + str(a))

    value = ler_arquivo()
    key_value = dict(zip(key, value))
    linha_key_value = dict(zip(linha_key, value))
    talk(linha_key_value)
    apagar_compromisso(key_value, len(value))


def apagar_compromisso(lista, quant_linha):
    try:
        command = ""
        with sr.Microphone() as source:
            talk("Por favor diga o numero da linha que deseja apagar")
            audio = recon.listen(source)
            command = recon.recognize_google(audio, language='pt')
            command = command.lower()
            if command != "":
                valid_numero_linha(command, quant_linha, lista)

    except:
        pass


def valid_numero_linha(command, quant_linha, lista):
    try:
        command = int(command)
        if type(command) == int and 0 < command < quant_linha + 1:
            apagar_linha(command, lista)
        else:
            talk("Linha não existe")
    except:
        talk('Não foi informado um numero valido')


def apagar_linha(linha_apagar, lista):
    print(lista)
    del lista[linha_apagar]
    print(lista)

    nova_lista = []

    for a, b in lista.items():
        nova_lista.append(b + '\n')
    arquivo = open('agenda.txt', 'w')
    for a in nova_lista:
        arquivo.write(a)
    arquivo.close()
    talk("compromisso apagado")


def main():
    try:
        command = ''
        while True:
            command = comando()
            print(command)
            if command in 'data' or command == 'que dia é hoje' or command in 'dia':
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
            elif command in 'hora' or command == 'que horas são':
                d1 = datetime.today().strftime('%H-%M')
                talk(d1)
                return
            elif 'Cara' in command or 'coroa' in command or command == 'cara ou coroa':
                if random.randint(1, 2) == 1:
                    talk("Saiu Cara")
                else:
                    talk("Saiu Coroa")
                return
            elif 'solteira' in command or command == 'você esta solteira':
                talk('Eu estou em um relacionamento com o wi-fi')
                return
            elif 'wikipédia' in command or command == 'pesquisar no wikipedia':
                pesquisa = wikipedia.summary(pesquisar_wikipedia())[0:150]
                talk(pesquisa)
                return
            elif 'limpar agenda' in command:
                limpar_agenda()
                return
            elif 'apagar compromisso' in command or command == 'apagar compromisso':
                listar_compromisso_dicionario()
                return
            elif 'advinha' in command or command == 'advinha o numero' or command == 'o numero':
                advinhe_o_numero()
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
