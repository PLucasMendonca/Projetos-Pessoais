from Interface import leiaFloat

def operacao():
    operacoes = ['*', '/', '+','-']
    while True:
        x = input('Digite uma operação: ').strip()
        if x in operacoes:
            return x
        print('Digite uma das operações válidas \n * -> Multiplicação \n + -> Soma\n - -> Subtração\n / -> Divisão')

def soma(x, x1):
    return x + x1

def diminuir(x, x1):
    return x - x1

def dividir(x, x1):
    while True:
        if x1 == 0:
            print('Não é possivel realizar divisão por 0')
            x1 = leiaFloat('Digite um novo número: ')
        else:
            break
    return x / x1

def multiplicar(x, x1):
    return x * x1