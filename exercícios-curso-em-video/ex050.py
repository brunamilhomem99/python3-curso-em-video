# Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem PARES.
# Se o valor digitado for ÍMPAR, desconsidere-o.

soma = 0
cont = 0
for i in range(1, 7):
    num = int(input('Digite um valor inteiro: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Você informou {cont} números pares e a soma foi de: \033[34m{soma}\033[m')
