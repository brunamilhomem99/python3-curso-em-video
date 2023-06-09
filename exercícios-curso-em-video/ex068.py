# Faça um programa que jogue par ou ímpar com o pc. O jogo será interrompido quando o jogador PERDER,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

margin = '-' * 20
print(f'{margin} Vamos jogar ÍMPAR ou PAR! {margin}')

wins = 0
while True:
    user_num = int(input('Digite um número: '))
    pc_num = randint(0, 50)
    total = pc_num + user_num
    user_guess = ' '
    while user_guess not in 'PI':
        user_guess = str(input('Escolha entre PAR ou ÌMPAR [I/P]: ')).strip().upper()[0]


    if user_guess == 'P':
        if user_num % 2 == 0:
            print('PARABÉNS! Você venceu!')
            wins += 1
        else:
            break
    elif user_guess == 'I':
        if user_num % 2 != 0:
            print('PARABÉNS! Você venceu!')
            wins += 1
        else:
            break

print(f'GAME OVER!\nVocê teve {wins} vitórias.')







