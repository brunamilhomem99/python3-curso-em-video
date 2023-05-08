# escreva um programa que faça o computador "pensar" em um número de 0 a 5 e peça para o user tentar descobrir qual foi
# o número escolhido pelo computador, printando na tela se o user venceu ou perdeu.

from random import randint  # biblioteca para randomizar o valor
from time import sleep  # biblioteca para dar um delay no output
num = randint(0, 5)
guess = int(input('Tente adivinhar um número de 0 a 5: '))
print('PROCESSANDO...')
sleep(2)
if guess == num:
    print('Parabéns, você acertou!')
else:
    print(f'Que pena, você errou! O número escolhido era {num}')
