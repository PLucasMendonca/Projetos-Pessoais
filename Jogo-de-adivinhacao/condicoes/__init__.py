from random import randint
from time import sleep
import os

def linha(tam):
    linha = '=' * (len(tam))
    print(linha)
    print(tam)
    print(linha)
    print()

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def resposta_correta(palpites,numero,chutes):
    linha(f"Parabéns! Você acertou em {palpites} palpites")
    sleep(1)
    print(f"O número que pensei foi {numero}\n")
    print(f"Seus palpites foram {chutes}\n")

    if  palpites <= 3:
        print("Nossa, você me humilhou!")
    elif 4 < palpites <= 7:
        print("Foi rápido até!")
    elif 7< palpites <= 10:
        print("Demorou um pouco, mas conseguiu!")
    else:
        print("Você ainda tentou bastante, hein? 😅")

def sair():
    print('\U0001F923 Pelo visto eu venci \U0001F923')
    sleep(2)
    print('\U0001F923 Até mais perdedor!!! \U0001F923')
    sleep(2)

def reiniciar_jogo(nivel):
    resposta = confirmar('\nVocê quer reiniciar o jogo? [S/N]: ')
    if resposta == "S":
        print("Reiniciando o jogo...")
        sleep(2)
        limpar()
        nivel()
    else:
        print("Voltando ao menu principal...")
        sleep(2)
        limpar()

def ajuda(x,y):
    if x < y :
        print('O número que escolhi é MAIOR... Tente novamente')
    elif x > y:
        print('O número que escolhi é MENOR... Tente novamente')

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError,TypeError):
            print('\033[31mERROR: por favor digite um número INTEIRO válido\033[m')
            continue
        except(KeyboardInterrupt):
            print('\nEntrada de dados interrompida pelo usuário')
            return 999
        else:
            return n
        
def confirmar(x):
    while True:
        try:
            resp = input(x).strip().upper()  # remove espaços e deixa maiúsculo
            if resp not in ['S', 'N']:
                raise ValueError("Digite apenas S ou N")
        except ValueError as e:
            print(f"\033[31mERROR: {e}\033[m")
            continue
        except KeyboardInterrupt:
            print("\nEntrada de dados interrompida pelo usuário")
            return 'N'   # pode retornar 'N' como padrão
        else:
            return resp
