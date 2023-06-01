# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep
a = int(input('\033[35mPrimeiro número:\033[m '))
b = int(input('\033[36mSegundo número:\033[m '))
escolha = 0
while escolha != 5:
    escolha = int(input('''[ \033[31m1\033[m ] somar;
[ \033[32m2\033[m ] multiplicar;
[ \033[35m3\033[m ] maior;
[ \033[33m4\033[m ] novos números;
[ \033[34m5\033[m ] sair do programa;
Escolha uma das opções acima: '''))
    if escolha == 1:
        print(f'A soma dos números escolhidos é \033[1m{a + b}\033[m.')
    elif escolha == 2:
        print(f'A multiplicação dos números escolhidos é \033[1m{a * b}\033[m.')
    elif escolha == 3:
        if a > b:
            print(f'O número {a} é maior.')
        else:
            print(f'O número {b} é maior.')
    elif escolha == 4:
        a = int(input('\033[35mPrimeiro número:\033[m '))
        b = int(input('\033[36mSegundo número:\033[m '))
    elif escolha == 5:
        print('\033[33mFinalizando...\033[m')
    else:
        print('Opção inválida. Você só pode escolher entre 1 e 5.')
        break
    sleep(2)
print('\033[1mFim do programa! Volte sempre.\033[m')
