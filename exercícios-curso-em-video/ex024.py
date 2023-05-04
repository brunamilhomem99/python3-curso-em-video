# Crie um programa que leia um nome de uma cidade e diga se ela começa ou não com a palavra "SANTO".

c = str(input('Digite o nome de uma cidade: ')).strip()
print(c[:5].upper() == 'SANTO')
