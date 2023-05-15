# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from datetime import date
a = int(input('Que ano gostaria de analisar? Digite 0 caso queira analisar o ano atual: '))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print(f'O ano \033[35m{a}\033[m é bissexto!')
else:
    print(f'O ano \033[35m{a}\033[m não é bissexto.')
