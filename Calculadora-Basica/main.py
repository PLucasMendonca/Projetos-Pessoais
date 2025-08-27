from Operacoes import *
from Interface import *

primeiroNum = leiaFloat('Digite o primeiro número: ')
opr = operacao()
segundoNum = leiaFloat('Digite o segundo número: ')

if opr == '*':
    x = multiplicar(primeiroNum,segundoNum)
    resultado(primeiroNum,opr,segundoNum,x)
elif opr == '+':
    x = soma(primeiroNum,segundoNum)
    resultado(primeiroNum,opr,segundoNum,x)
elif opr == '/':
    x = dividir(primeiroNum, segundoNum)
    resultado(primeiroNum,opr,segundoNum,x)
elif opr == '-':
    x = diminuir(primeiroNum,segundoNum)
    resultado(primeiroNum,opr,segundoNum,x)