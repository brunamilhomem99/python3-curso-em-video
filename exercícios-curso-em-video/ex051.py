# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))

termos = [p + i * r for i in range(10)]
print(termos)