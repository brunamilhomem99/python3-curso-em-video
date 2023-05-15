# Crie um programa que leia um nome de uma cidade e diga se ela começa ou não com a palavra "SANTO".

c = str(input('\033[30mDigite o nome de uma cidade:\033[m ')).strip()
print(c[:5].upper() == 'SANTO')
