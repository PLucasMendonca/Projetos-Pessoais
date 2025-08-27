def resultado(x,x1,x2,x3):
    print(f'A operação {x} {x1} {x2} é {x3:.2f}')


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERROR. Por favor, digite um número inteiro váliido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n Entrada de dados interrompida pelo usuário')
            return 0
        else:
            return n
