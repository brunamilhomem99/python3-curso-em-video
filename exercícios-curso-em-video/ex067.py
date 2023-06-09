# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo user.
# O programa será interrompido quando o número solicitado for negativo.

cont = num = 0

while True:
    num = int(input('Digite um número: '))

    print('=' * 20)
    for i in range(1, 11):

        if num < 0:
            print('Programa encerrado, volte sempre!')
            break

        print(f'{num} x {i} = {num * i}')
    print('=' * 20)