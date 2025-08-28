from condicoes import *
from Interface import *
from time import sleep



while True:
    escolha = menu(['Nivel Facil', 'Nível Médio', 'Nível Dificil', 'Sair do Jogo'])

    if escolha == 1:
        facil()
    elif escolha == 2:
        medio()
    elif escolha == 3:
        dificil()
    elif escolha == 4:
        print('Até mais, Obrigado por jogar!')
        break
    else:
        print(f'\033[31mERROR: A opção \033[34m{escolha}\033[m \033[31mnão é uma das opções a cima, Escolha corretamente!\033[m')
        sleep(3)
