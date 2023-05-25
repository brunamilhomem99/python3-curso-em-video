# Crie um programa que leia uma frase qualquer e diga se ela é
# um PALÍNDROMO (igual de trás para frente). desconsiderando os espaços.

from dataclasses import replace

frase = str(input('Digite uma frase: ')).strip().upper()
f = frase.replace(' ', '') 
inverso = ''
for letra in range(len(f) -1, -1, -1):
    inverso += f[letra]
print(f'O inverso de \033[31m{f}\033[m é \033[34m{inverso}\033[m')
if inverso == f:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo.')