# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por
# km para viagens de até 200km e R$0,45 para viagens mais longas.

d = float(input('Qual será a distância da viagem em \033[34mkm\033[m? '))
if d <= 200:
    print('Para viagens de \033[34m{} Km/h\033[m, o valor da passagem será \033[32mR${:.2f}\033[m'.format(d, d * 0.50))
else:
    print('Para viagens de \033[34m{} Km/h\033[m, o valor da passagem será \033[32mR${:.2f}\033[m'.format(d, d * 0.45))
