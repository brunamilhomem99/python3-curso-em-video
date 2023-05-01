# O mesmo professor quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import sample
alunos = ['Hermione', 'Ron', 'Harry', 'Neville']
print(f'A ordem de apresentação dos alunos será: {sample(alunos, k=len(alunos))}')




