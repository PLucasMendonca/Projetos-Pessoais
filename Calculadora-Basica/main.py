
def soma(x, x1):
    return x + x1

def diminuir(x, x1):
    return x - x1

def dividir(x, x1):
    return x / x1

def multiplicar(x, x1):
    return x * x1

n = int(input('Digite o primeiro número: '))
n1 = (input('Digite uma operação: '))
n2 = int(input('Digite o segundo número: '))

if n1 == '*':
    x = multiplicar(n,n2)
    print(x)
elif n1 == '+':
    x = soma(n,n2)
    print(x)
elif n1 == '/':
    x = dividir(n, n2)
    print(x)
elif n1 == '-':
    x = diminuir(n,n2)
    print(x)
else:
    print('Digitou nenhuma operação válida')