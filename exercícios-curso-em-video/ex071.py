# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte qual será o
# valor a ser sacado (número inteiro) e o programa vai informar quantas células de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('=' * 30)
print('{:^30}'.format(' CAIXA ELETRÔNICO '))
print('=' * 30)
saque = int(input('Qual valor deseja sacar? R$'))

total = saque
ced = 50
total_ced = 0
while True:
    if total >= ced:
        total -= ced
        total_ced += 1
    else:
        if total_ced > 0:
            print(f'Total de {total_ced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        total_ced = 0
        if total == 0:
            break
