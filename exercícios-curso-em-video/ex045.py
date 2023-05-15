# Crie um programa que faça o pc jogar JOKENPÔ com você.

import random
print('\033[1;37m-=-\033[m' * 7)
print('\033[33mLETS\033[m \033[35mPLAY\033[m \033[36mJOKENPÔ!\033[m')
print('\033[1;37m-=-\033[m' * 7)
jogada_user = str(input('Escolha entre PEDRA PAPEL ou TESOURA: ')).upper()
elementos = ['PEDRA', 'PAPEL', 'TESOURA']
jogada_pc = random.choice(elementos)
if jogada_user == 'PEDRA'.upper() and jogada_pc == 'PAPEL':
    print('\033[1;32mParabéns, você ganhou!\033[m')
elif jogada_user == 'PAPEL'.upper() and jogada_pc == 'PEDRA':
    print('\033[1;31mGame Over\033[m')
elif jogada_user == 'PEDRA'.upper() and jogada_pc == 'TESOURA':
    print('\033[1;32mParabéns, você ganhou!\033[m')
elif jogada_user == 'TESOURA'.upper() and jogada_pc == 'PEDRA':
    print('\033[1;31mGame Over\033[m')
elif jogada_user == 'TESOURA'.upper() and jogada_pc == 'PAPEL':
    print('\033[32mParabéns, você ganhou!\033[m')
elif jogada_user == 'PAPEL'.upper() and jogada_pc == 'TESOURA':
    print('\033[31mGame Over\033[m')
elif jogada_user == jogada_pc:
    print('\033[33mEMPATE!')