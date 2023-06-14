# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o amior valor que estão na tupla

from random import sample
random_numbers = sample(range(1, 11), 5)
tupla = tuple(random_numbers)
print(f'Números sorteados: {tupla}')

valor = menor = maior = 0
for i in tupla:
    if valor == tupla[1]:
        maior = menor = tupla
    else:
        if i < menor:
            menor = i
        elif i > maior:
            maior = i
print(f'Maior: {maior}\nMenor: {menor}')
