# escreva um programa que faça o computador "pensar" em um número de 0 a 5 e peça para o user tentar descobrir qual foi
# o número escolhido pelo computador, printando na tela se o user venceu ou perdeu.

from random import randint  # biblioteca para randomizar o valor
from time import sleep  # biblioteca para dar um delay no output
num = randint(0, 5)
guess = int(input('Tente adivinhar um número de \033[33m0\033[m a \033[36m5\033[m: '))
print('\033[31mPROCESSANDO...\033[m')
sleep(2)
if guess == num:
    print('\033[32mParabéns, você acertou!\033[m')
else:
    print(f'\033[31mQue pena, você errou! O número escolhido era {num}\033[m')
