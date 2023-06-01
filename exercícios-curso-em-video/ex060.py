# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# ex: 5! = 5x4x3x2x1 = 120

blue = '\033[34m'
yellow = '\033[33m'
reset = '\033[m'

n = int(input('Digite um número para saber seu fatorial: '))
c = n
fac = 1
print(f'{blue}Calculando {n}!{reset}', end=' ')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    fac *= c
    c -= 1
print(f'{yellow}{fac}{reset}', end='')
