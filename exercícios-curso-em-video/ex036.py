# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos
# anos ele irá pagar o imóvel.

# Calcule o valor da prestação mensal, sabendo que ela não pode
# exceder 30% do salário ou então o empréstimo será negado.

house = float(input('\033[1;30mQual o valor da casa que você deseja comprar? R$\033[m'))
salary = float(input('\033[1;30mQual é valor do seu salário? R$\033[m'))
years = int(input('\033[1;30mEm quantos anos você irá pagar o imóvel? \033[m'))
installment = house / (years * 12)

if installment > salary * (30 / 100):
    print(
        'A prestação de \033[31;40mR${:.2f}\033[m excede mais de 30% do seu salário de \033[31mR${:.2f}\033[m. Sinto '
        'informar que o empréstimo não será concedido.'.format(installment, salary))
else:
    print(
        f'Certo, o empréstimo será concedido. Você terá que pagar \033[31m{years * 12}x de R${installment:.2f}\033[m')
