# Melhore o jogo do desafio 028, em que o pc vai "pensar" em um número entre 0 e 10. Só que agora
# o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

# sequências de escape ANSI
red = '\033[31m'
green = '\033[32m'
reset = '\033[m'

from random import randint
acertou = False
num = randint(0, 10)
tentativas = 0
while not acertou:
    palpite = int(input('Adivinhe o número: '))
    tentativas += 1
    if palpite < num:
        print(f'{red}Maior{reset}. Tente outro!')
    elif palpite > num:
        print(f'{red}Menor{reset}. Tente outro!')
    else:
        break
print(f'{green}Acertou com {tentativas} tentativas. Parabéns!{reset}')