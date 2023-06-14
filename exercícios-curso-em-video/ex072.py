# Crie um programa que tenha uma tupla totalemente preechida com contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

red = '\033[31m'
reset = '\033[m'

numbers = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
          'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    user_num = int(input('Digite um número de 0 a 20 para ver seu nome por extenso: '))
    if 0 <= user_num <= 20:
        break
print(f'Você digitou o número {red}{numbers[user_num]}{reset}')
