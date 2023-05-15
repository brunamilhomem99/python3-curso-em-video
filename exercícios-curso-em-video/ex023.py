# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# ex: input: 1834; output: unidade: 4. dezena: 3. centena: 8. milhas: 1

num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Unidade: \033[33m{u}\033[m\nDezena: \033[33m{d}\033[m\nCentena: \033[33m{c}\033[m\nMilhar: \033[33m{m}\033[m')
