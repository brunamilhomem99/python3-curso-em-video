# Crie um um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida

a = float(input('\033[1;30mPrimeira nota: \033[m'))
b = float(input('\033[1;30mSegunda nota: \033[m'))

avg = (a + b) / 2
if 7 > avg >= 5:
    print('\033[31mCom média {:.1f} você está de RECUPERAÇÃO, estude mais na próxima!\033[m'.format(avg))
elif avg < 5:
    print('\033[31mCom média {:.1f} você está REPROVADO\033[m'.format(avg))
elif avg >= 7:
    print('\033[36mCom média {:.1f} você está APROVADO! Contiue assim.\033[m'.format(avg))
