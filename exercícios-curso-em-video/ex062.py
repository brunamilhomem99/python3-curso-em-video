# Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.

blue = '\033[34m'
red = '\033[31m'
purple = '\033[35m'
reset = '\033[m'

p = int(input(f'{blue}Primeiro termo:{reset} '))
r = int(input(f'{red}Razão da PA:{reset} '))
termo = p
cont = 1
mais_termos = 10
total = 0
while mais_termos != 0:
    # adicionando mais termos a partir do 10, conforme a escolha do usuário
    total += mais_termos
    while cont <= total:
        print(f'{termo} - ', end='')
        termo += r
        cont += 1
    print(f'{purple}PAUSA{reset}')
    mais_termos = int(input('Quantos termos mais você quer mostrar? '))
print(f'{purple}FIM{reset}')