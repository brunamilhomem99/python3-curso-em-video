# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
dec = p + (10 - 1) * r
for i in range(p, dec + r, r):
    print(f'{i}', end=' ')