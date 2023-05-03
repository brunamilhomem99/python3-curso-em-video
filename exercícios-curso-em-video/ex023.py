# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# ex: input: 1834; output: unidade: 4. dezena: 3. centena: 8. milhas: 1

num = str(input('Digite um número de 0 a 9999: '))
print(f'Unidade: {num[3]}\nDezena: {num[2]}\nCentena: {num[1]}\nMilhar: {num[0]}')
