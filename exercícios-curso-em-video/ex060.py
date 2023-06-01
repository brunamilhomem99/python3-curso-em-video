# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# ex: 5! = 5x4x3x2x1 = 120

from math import factorial
n = int(input('Digite um número para saber seu fatorial: '))
c = 1
while c == 1:
    if n != 0:
        print(f'Resultado: \033[36m{n}\033[m! = \033[36m{factorial(n)}\033[m')
        break
