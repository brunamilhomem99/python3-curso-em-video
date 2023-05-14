# Um professor quer sortear um dos seus alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
from random import choice
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
alunos = [n1, n2, n3, n4]
print(f'O aluno escolhido para para apagar o quadro foi: \033[34m{choice(alunos)}\033[m')

