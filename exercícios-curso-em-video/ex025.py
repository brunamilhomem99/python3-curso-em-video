# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Digite seu nome completo: ')).strip()
print('Se nome tem Silva? \033[34m{}\033[m'.format('silva' in nome.lower()))
