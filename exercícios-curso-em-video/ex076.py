# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados de forma tabular.

blue = '\033[34m'
reset = '\033[m'

produtos = ('Cardeno', '35,00', 'Caneta esferográfica', '2,00', 'Marca-texto', '3,50', 'Borracha', '1,50', 'Apontador',
            '2,50', 'Agenda', '15,99')

print('-' * 37)
print(f'{blue}CATÁLOGO DE MATERIAIS ESCOLARES{reset}')
print('-' * 37)

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else: 
        print(f'R${produtos[pos]:.>5}')
print('-' * 37)
