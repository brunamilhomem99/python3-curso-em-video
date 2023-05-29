# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input(f'Peso {i}: '))
    if i == 1:
        maior = peso
        menor = peso
    else: 
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de \033[34m{maior}Kg\033[m.\nO menor peso lido foi de \033[36m{menor}Kg\033[m.')