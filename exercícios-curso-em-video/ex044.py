# Elabore um programa que calcule um valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# À vista dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# Em até duas vezes no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

print('\033[1;37m-=-\033[m' * 35)
print('Modalidades de Pagamento: \033[36mDinheiro/cheque (1)\033[m | \033[35mCartão: (2)\033[m | \033[33mAté 2x no '
      'Cartão (3) | \033[31m3x ou mais no Cartão (4)')
print('\033[1;37m-=-\033[m' * 35)
p = int(input('Escolha uma das modalidades de pagamento acima de acordo com o dígito: '))
v = float(input('Valor do produto: \033[32mR$\033[m'))
if p == 1:
      print('Com um desconto de 10%, o valor do produto será R${:.2f}'.format(v - (v * 10 / 100)))
elif p == 2:
      print('Com um desconto de 5%, o valor do produto será R${:.2f}'.format(v - (v * 5 / 100)))
elif p == 3:
      print(f'Em até 2x no Cartão o valor do produto continuará R${v}')
elif p == 4:
      print('Em até 3x no cartão serão acrescentados 20% de juros no valor total do produto.')