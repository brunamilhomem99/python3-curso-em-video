# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n = int(input('Digite um número: '))
if n % n == 0 and n != 1:
    print('O número é primo.')
else:
    print('O número não é primo.')