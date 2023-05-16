# Elabore um programa que calcule um valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# À vista dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# Em até duas vezes no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

print('''Modalidades de Pagamento: 
[ 1 ] \033[36mDinheiro/cheque\033[m
[ 2 ] \033[35mCartão\033[m
[ 3 ] \033[33mAté 2x no Cartão\033[m
[ 4 ] \033[34m3x ou mais no Cartão\033[m''')

v = float(input('Valor do produto: \033[32mR$\033[m'))
p = int(input('Escolha uma das modalidades de pagamento acima de acordo com o dígito: '))
if p == 1:
    total = v - (v * 10 / 100)
    print('Com um desconto de 10%, o valor do produto será R${:.2f}'.format(total))
elif p == 2:
    total = v - (v * 5 / 100)
    print('Com um desconto de 5%, o valor do produto será R${:.2f}'.format(total))
elif p == 3:
    print(f'Em até 2x no Cartão o valor do produto continuará R${v}')
elif p == 4:
    total = v + (v * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} com juros. No fina custará R${}'.format(totparc, parcela, total))
else: 
    print('\033[31mOpção inválida. Tente novamente!\033[m')
