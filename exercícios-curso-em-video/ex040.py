# Crie um um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida

a = float(input('\033[1;37mPrimeira nota: \033[m'))
b = float(input('\033[1;37mSegunda nota: \033[m'))

average = (a + b) / 2
if average < 5:
    print('\033[31mVocê está de recuperação, estude mais na próxima!\033[m')
elif average >= 5:
    print('\033[36mParabéns, você está acima da média! Contiue assim.\033[m')
