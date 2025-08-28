from random import randint
from time import sleep
def facil():
    numero = randint(0,15)
    print('Começando jogo de adivinhação no modo Fácil')
    sleep(3)
    print('Tente adivinhar o número que estou pensando entre 0 e 15')
    palpite = 0
    acertou = False
    while not acertou:
        jogador = leiaInt('Qual o seu palpite (Para sair digite 999):')
        palpite +=1
        if jogador == numero:
            acertou == True
            print(f'Parabens você acertou em {palpite} palpites')
            if 1 < palpite <= 3:
                print('Nossa voce me humilhou')
            elif 3 < palpite <= 10:
                print('Demorou um pouco mas foi')
            else:
                print('Nossa você ainda tentou isso tudo')
            break
        elif jogador == 999:
            sair()
            break
        elif jogador < 0 or jogador > 15:
            print(f'O número {jogador} não é válido...\nO NÚMERO É ENTRE 0 E 15...')
            sleep(2)
        else:
            if jogador < numero :
                print('O número é MAIOR... Tente novamente')
            elif jogador > numero:
                print('O número é MENOR... Tente novamente')
        

def medio():
    numero = randint(0,20)
    print('Começando jogo de adivinhação no modo Médio')
    sleep(3)
    print('Tente adivinhar o número que estou pensando entre 0 e 20 (Sem Dicas)')
    palpite = 0
    acertou = False
    ajuda_ativa = False
    while not acertou:
        jogador = leiaInt('Qual o seu palpite (Para sair digite 999):')
        palpite +=1
        if jogador == numero:
            acertou == True
            print(f'Parabens você acertou em {palpite} palpites')
            if 1 < palpite <= 3:
                print('Nossa voce me humilhou')
            elif 3 < palpite <= 15:
                print('Demorou um pouco mas foi')
            else:
                print('Nossa você ainda tentou isso tudo')
            break
        elif jogador == 999:
            sair()
            break
        elif jogador < 0 or jogador > 20:
            print(f'O número {jogador} não é válido...\nO NÚMERO É ENTRE 0 E 20...')
            sleep(1)
        else:
            if ajuda_ativa:
                ajuda(jogador, numero)
            elif palpite >= 20 and palpite % 5 == 0:
                while True:
                    resp = input('Você quer uma ajuda fraco ? [S/N]: ').strip().upper()[0]
                    if resp in ['S', 'N']:
                        break
                    print('Resposta inválida! Digite apenas S ou N!')
                if resp == 'S':
                    print(f'Ok irei te ajudar...')
                    ajuda_ativa = True
                    ajuda(jogador, numero)
                else:
                    print('Ok, sem ajuda então')

def dificil():
    print('Em progesso')

def sair():
    print('\U0001F923 Pelo visto eu venci \U0001F923')
    sleep(2)
    print('\U0001F923 Até mais perdedor!!! \U0001F923')
    sleep(2)

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

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError,TypeError):
            print('\033[31mERROR: por favor digite um número INTEIRO válido\033[m')
            continue
        except(KeyboardInterrupt):
            print('\nEntrada de dados interrompida pelo usuário')
            return 0
        else:
            return n