# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n = int(input('Digite um número: '))
tot = 0
for i in range(1, n + 1):
    if n % i == 0:
        print('\033[34m ', end='')
        tot += 1
    else:
        print('\033[m ', end='')
    print(f'{i}', end='')
print(f'\n\033[mO número {n} foi divisível {tot} vezes', end='')
if tot == 2:
    print(', portanto \033[31mé primo\033[m.')
else:
    print(', portanto \033[31mnão é primo\033[m.')