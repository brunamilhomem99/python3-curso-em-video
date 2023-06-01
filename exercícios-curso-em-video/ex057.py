# Faça um programa que leia o gênero de uma pessoa, mas só aceite os valores 'M', 'F' ou 'NB'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

# sequências de escape ANSI
yellow = '\033[33m'
blue = '\033[34m'
purple = '\033[35m'
cyan = '\033[36m'
reset = '\033[m'

while True:
    genero = str(input(f'Com que gênero você se identifica? [{yellow}M{reset}, {blue}F{reset}, {purple}NB{reset}]: ')).strip().upper()
    if genero in ['M', 'F', 'NB']:
        break
print(f'{cyan}Que legal! Seja bem vindo(a,e).{reset}')
