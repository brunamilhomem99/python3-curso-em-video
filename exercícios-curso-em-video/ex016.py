# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
from math import trunc
num = float(input('Digite um número quebrado: '))
print(f'A porção inteira do número dado é \033[1m{trunc(num)}\033[m')
