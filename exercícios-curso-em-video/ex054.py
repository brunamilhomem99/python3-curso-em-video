# Crie um programa que leia o ano de nascimento de 7 pessoas. No final, mostre quantas pesssoas
# ainda não atingiram a maioridade e quantas já são maiores (21 anos).

from datetime import date
ano_atual = date.today().year
totmenor = 0
totmaior = 0
for i in range(1, 8):
    ano = int(input(f'Data de nascimento {i}: '))
    idade = ano_atual - ano
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Ao todo tivemos {totmaior} pessoas maiores de idade e {totmenor} pessoas menores.')