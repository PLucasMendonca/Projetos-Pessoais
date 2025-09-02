from condicoes import leiaInt
import os


def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')


def linha(tam = 90):
    return '=' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(90))
    print(linha())

def menu(lista):
    cabecalho('Bem vindo ao Jogo de Adivinhação')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c +=1
    print(linha())
    opc = leiaInt('Escolha a dificuldade:')
    limpar()
    return opc