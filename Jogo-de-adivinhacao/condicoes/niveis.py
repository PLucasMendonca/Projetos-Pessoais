from condicoes import *

def facil():
    numero = randint(0, 15)
    chutes = []

    linha("Começando jogo de adivinhação no modo Fácil")
    sleep(2)
    print("REGRAS: Tente adivinhar o número que estou pensando entre 0 e 15\n")

    palpites = 0

    while True:
        numero_jogador = leiaInt("Qual o seu palpite (Parar o jogo digite 999): ")

        if numero_jogador == 999:
            sair()
            break

        if numero_jogador < 0 or numero_jogador > 15:
            print(f"O número {numero_jogador} não é válido... \nO NÚMERO É ENTRE 0 E 15...")
            sleep(2)
            continue

        if numero_jogador in chutes:
            print("Você já tentou esse número...")
            continue

        chutes.append(numero_jogador)
        palpites += 1

        if numero_jogador == numero:
            resposta_correta(palpites,numero,chutes)
            break
        else:
            ajuda(numero_jogador, numero)

    reiniciar_jogo(facil)

def medio():
    numero = randint(0,20)
    chutes = []

    linha('Começando jogo de adivinhação no modo Médio')
    sleep(2)
    print('REGRAS: Tente adivinhar o número que estou pensando entre 0 e 20 (Sem Dicas)\n')

    palpites = 0
    ajuda_ativa = False

    while True:
        numero_jogador = leiaInt('Qual o seu palpite (Parar o jogo digite 999):')

        if numero_jogador == 999:
            sair()
            break

        if numero_jogador < 0 or numero_jogador > 20:
            print(f'O número {numero_jogador} não é válido...\nO NÚMERO É ENTRE 0 E 20...')
            sleep(2)
            continue
        
        if numero_jogador in chutes:
            print("Você já tentou esse número...")
            continue

        chutes.append(numero_jogador)
        palpites += 1

        if numero_jogador == numero:
            resposta_correta(palpites,numero,chutes)
            break        
        else:
            if ajuda_ativa:
                ajuda(numero_jogador, numero)
            elif palpites >= 5 and palpites % 5 == 0:
                while True:
                    resp = input('Você quer uma ajuda fraco ? [S/N]: ').strip().upper()[0]
                    if resp in ['S', 'N']:
                        break
                    print('Resposta inválida! Digite apenas S ou N!')
                if resp == 'S':
                    print(f'Ok irei te ajudar...')
                    sleep(3)
                    ajuda_ativa = True
                    ajuda(numero_jogador, numero)
                else:
                    print('Ok, sem ajuda então')

    reiniciar_jogo(medio)

def dificil():
    numero = randint(0,15)
    chutes = []

    linha('Começando jogo de adivinhação no modo Difícil')
    sleep(2)
    print('Tente adivinhar o número que estou pensando entre 0 e 30 (Terá apenas 5 chances!)\n')

    palpites = 5

    while palpites != 0:
        numero_jogador = leiaInt('Qual o seu palpite (Parar o jogo digite 999):')

        if numero_jogador == 999:
            sair()
            break

        if numero_jogador < 0 or numero_jogador > 30:
            print(f'O número {numero_jogador} não é válido...\nO NÚMERO É ENTRE 0 E 30...')
            sleep(2)
            continue
        
        if numero_jogador in chutes:
            print("Você já tentou esse número...")
            print("Vou te dar uma colher de chá e não vou remover este palpite")
            palpites +=1
            continue
        chutes.append(numero_jogador)

        if numero_jogador == numero:
            usados = 5 - palpites + 1
            print(f'\nVocê acertou antes de acabar suas chances')
            resposta_correta(usados, numero, chutes)
            break
        else:
            ajuda(numero_jogador, numero)
        
        palpites -= 1

        print(f'Voce tem {palpites} chances') 

        if palpites == 4:
            print('Só o começo, bora lá')
        elif palpites == 3:
            print('Vou ganhar fácil')
        elif palpites == 2:
            print('Cuidado que ta acabando')
        elif palpites == 1:
            print('Sua ultima chance, se concentra ')
        else:
            print('PERDEDOR!')
            print(f'O número que pensei era {numero}')
            print()
    reiniciar_jogo(dificil)
   