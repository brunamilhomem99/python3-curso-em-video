# Um professor quer sortear um dos seus alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
from random import choice
alunos = ['Jake', 'Laurie', 'Jungkook', 'Luna']
print(f'O aluno escolhido para para apagar o quadro foi: {choice(alunos)}')

