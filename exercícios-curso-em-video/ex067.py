# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo user.
# O programa será interrompido quando o número solicitado for negativo.

yellow = '\033[33m'
reset = '\033[m'

cont = num = 0

while True:
    num = int(input('Digite um número: '))

    print(f'{yellow}={reset}' * 20)
    for i in range(1, 11):

        if num < 0:
            print('Programa encerrado, volte sempre!')
            break

        print(f'{num} {yellow}x{reset} {i} {yellow}={reset} {num * i}')
    print(f'{yellow}={reset}' * 20)