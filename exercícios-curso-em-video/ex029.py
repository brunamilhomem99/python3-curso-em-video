# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele
# foi multado. A multa deve custar R$7,00 por cada km acima do limite.

v = float(input('Qual a velocidade do carro em km/h? '))
if v > 80:
    print('Você ultrapassou o limite de 80Km/h. Sinto informar que receberá uma multa de R${:.2f}'.format((v - 80) * 7))
else:
    print('Ótimo, você esta dentro dos limites de velocidade, continue assim!')
