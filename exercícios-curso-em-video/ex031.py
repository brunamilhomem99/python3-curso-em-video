# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por
# km para viagens de até 200km e R$0,45 para viagens mais longas.

d = float(input('Qual será a distância da viagem em km? '))
if d <= 200:
    print('Para viagens de {} Km/h, o valor da passagem será R${:.2f}'.format(d, d * 0.50))
else:
    print('Para viagens de {} Km/h, o valor da passagem será R${:.2f}'.format(d, d * 0.45))
