# Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem PARES.
# Se o valor digitado for ÍMPAR, desconsidere-o.

soma = 0
for i in range(1, 7):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        soma = soma + num
print(f'\033[34m{soma}\033[m')
