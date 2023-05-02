# O mesmo professor quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
alunos = [n1, n2, n3, n4]
shuffle(alunos)
print('A ordem de apresentação dos alunos será: ')
print(alunos)




