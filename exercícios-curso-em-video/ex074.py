# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o amior valor que estão na tupla

from random import sample

random_numbers = (sample(range(1, 11), 5))

print(f'Números sorteados: {random_numbers}')
print(f'Maior valor: {max(random_numbers)}\nMenor valor: {min(random_numbers)}')
