# Melhore o jogo do desafio 028, em que o pc vai "pensar" em um número entre 0 e 10. Só que agora
# o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
c = 1
num = randint(0, 10)
while c == 1:
    palpite = int(input('Adivinhe o número: '))
    if palpite == num:
        break
print('Parabéns, você acertou!')