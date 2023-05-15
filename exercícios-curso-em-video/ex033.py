# Faça um programa que leia três números e mostre qual é o MAIOR e qual é o MENOR.

a = float(input('Primeiro valor: '))
b = float(input('Segundo valor: '))
c = float(input('Terceiro valor: '))

# verificando o menor número
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# verificando o maior número
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'\033[33mMaior valor:\033[m {maior}\n\033[34mMenor valor:\033[m {menor}')
