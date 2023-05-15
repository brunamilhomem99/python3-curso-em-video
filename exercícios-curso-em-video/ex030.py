# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.

num = int(input('Digite um número inteiro: '))
if num % 2 == 0:
    print(f'O número \033[36m{num}\033[m é \033[4mpar\033[m.')
else:
    print(f'O número \033[36m{num}\033[m é \033[4mímpar\033[m.')
