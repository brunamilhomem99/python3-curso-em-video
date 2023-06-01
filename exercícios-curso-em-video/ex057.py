# Faça um programa que leia o gênero de uma pessoa, mas só aceite os valores 'M', 'F' ou 'NB'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

c = 'F'
while c == 'F':
    genero = str(input('Com que gênero você se identifica? [M, F, NB]: ')).upper()
    if genero in ['M', 'F', 'NB']:
        break
print('Que legal!')
