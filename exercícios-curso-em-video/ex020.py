# O mesmo professor quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
n1 = str(input('\033[31mPrimeiro nome: \033[m'))
n2 = str(input('\033[32mSegundo nome: \033[m'))
n3 = str(input('\033[34mTerceiro aluno: \033[m'))
n4 = str(input('\033[35mQuarto aluno: \033[m'))
alunos = [n1, n2, n3, n4]
shuffle(alunos)
print('A ordem de apresentação dos alunos será: ')
print(alunos)




