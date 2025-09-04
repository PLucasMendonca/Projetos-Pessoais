from condicoes import *

def facil():
    numero = randint(0, 15)
    chutes = []
    linha("Começando jogo de adivinhação no modo Fácil")
    sleep(2)
    print("REGRAS: Tente adivinhar o número que estou pensando entre 0 e 15\n")

    palpites = 0

    while True:
        jogador = leiaInt("Qual o seu palpite (Parar o jogo digite 999): ")

        if jogador == 999:
            sair()
            break

        if jogador < 0 or jogador > 15:
            print(f"O número {jogador} não é válido. O NÚMERO É ENTRE 0 E 15...")
            sleep(2)
            continue

        if jogador in chutes:
            print("Você já tentou esse número...")
            continue

        chutes.append(jogador)
        palpites += 1

        if jogador == numero:
            resposta_correta(palpites,numero,chutes)
            break
        else:
            dica = "MAIOR" if jogador < numero else "MENOR"
            print(f"O número é {dica}... Tente novamente!")

    reiniciar_jogo(facil)

def medio():
    numero = randint(0,20)
    print('Começando jogo de adivinhação no modo Médio')
    sleep(3)
    print('REGRAS\nTente adivinhar o número que estou pensando entre 0 e 20 (Sem Dicas)')
    palpite = 0
    acertou = False
    ajuda_ativa = False
    while not acertou:
        jogador = leiaInt('Qual o seu palpite (Parar o jogo digite 999):')
        palpite +=1
        if jogador == numero:
            acertou == True
            print(f'Parabens você acertou em {palpite} palpites')
            sleep(2)
            print(f'O número em que pensei foi realmente {numero}')
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
            elif palpite >= 10 and palpite % 5 == 0:
                while True:
                    resp = input('Você quer uma ajuda fraco ? [S/N]: ').strip().upper()[0]
                    if resp in ['S', 'N']:
                        break
                    print('Resposta inválida! Digite apenas S ou N!')
                if resp == 'S':
                    print(f'Ok irei te ajudar...')
                    sleep(3)
                    ajuda_ativa = True
                    ajuda(jogador, numero)
                else:
                    print('Ok, sem ajuda então')
    reiniciar_jogo(medio)

def dificil():
    numero = randint(0,15)
    print('Começando jogo de adivinhação no modo Difícil')
    sleep(3)
    print('Tente adivinhar o número que estou pensando entre 0 e 30 (Terá apenas 5 chances!)')
    palpite = 5
    while palpite != 0:
        jogador = leiaInt('Qual o seu palpite (Parar o jogo digite 999):')
        palpite -=1
        print(f'Voce tem {palpite} chances')
        if jogador == numero:
            print(f'Parabens você acertou antes de acabar suas chances')
            print(f'O número em que pensei foi realmente {numero}')
            break
        elif jogador == 999:
            sair()
            break
        elif jogador < 0 or jogador > 30:
            print(f'O número {jogador} não é válido...\nO NÚMERO É ENTRE 0 E 30...')
            sleep(2)
        else:
            if jogador < numero :
                print('O número é MAIOR... Tente novamente')
            elif jogador > numero:
                print('O número é MENOR... Tente novamente')
        
        if palpite == 4:
            print('')
        elif palpite ==3:
            print('Vou ganhar fácil')
        elif palpite ==2:
            print('Cuidado que ta acabando')
        elif palpite ==1:
            print('Sua ultima chance, se concentra ')
        else:
            print('PERDEDOR!')
            print(f'O número que pensei era {numero}')
            print()
    reiniciar_jogo(dificil)
   