# Refaça o desafio 051. Lendo o primeiro termo e a razão de uma PA, mostrando
# os 10 primeiros termos da progressão aritmética usando a estrutra while.

blue = '\033[34m'
red = '\033[31m'
purple = '\033[35m'
reset = '\033[m'

p = int(input(f'{blue}Primeiro termo:{reset} '))
r = int(input(f'{red}Razão da PA: :{reset} '))
termo = p
cont = 1
while cont <= 10:
    print(f'{termo} - ', end='')
    termo += r
    cont += 1
print(f'{purple}FIM{reset}')