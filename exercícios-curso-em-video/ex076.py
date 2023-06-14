# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados de forma tabular.

produtos = ('Cardeno', '35,00', 'Caneta esferográfica', '2,00', 'Marca-texto', '3,50', 'Borracha', '1,50', 'Apontador',
            '2,50', 'Agenda', '15,99')

print('-' * 30)
print('CATÁLOGO DE MATERIAIS ESCOLARES')
print('-' * 30)

print(f'''
{produtos[0]}{'.' * 20} R${produtos[1]}
{produtos[2]}{'.' * 20} R${produtos[3]}
{produtos[4]}{'.'* 20} R${produtos[5]}
{produtos[6]}{'.' * 20} R${produtos[7]}
{produtos[8]}{'.' * 20} R${produtos[9]}
{produtos[10]}{'.' * 20} R${produtos[11]}
''')
