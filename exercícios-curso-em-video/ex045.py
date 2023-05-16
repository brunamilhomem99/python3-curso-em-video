# Crie um programa que faça o pc jogar JOKENPÔ com você.

from random import randint
elementos = ('pedra', 'papel', 'tesoura')
jogada_pc = randint(0, 2)
jogada_user = int(input('''Escolha entre 
[ 0 ]PEDRA 
[ 1 ]PAPEL
[ 2 ]TESOURA
Sua opção: '''))
print(f'Computador jogou {elementos[jogada_pc]}')
print(f'Humano jogou {elementos[jogada_user]}')

if jogada_pc == 0:  # computador jogou PEDRA
    if jogada_user == 0:
        print('EMPATE')
    elif jogada_user == 1:
        print('Você ganhou, PARABÉNS!')
    elif jogada_user == 2:
        print('\033[31mGAME OVER\033[m')
    else:
        print('Joagada Inválida')
elif jogada_pc == 1:
    if jogada_user == 0:
        print('\033[31mGAME OVER\033[m')
    elif jogada_user == 1:
        print('EMPATE')
    elif jogada_user == 2:
        print('Você ganou, PARABENS!')
    else: 
        print('Jogada Inválida')
elif jogada_pc == 2:
    if jogada_user == 0:
        print('Você ganhou, PARABÉNS!')
    elif jogada_user == 1:
        print('\033[31mGAME OVER\033[m')
    elif jogada_user == 2:
        print('EMPATE')
    else:
        print('Jogada Inválida')