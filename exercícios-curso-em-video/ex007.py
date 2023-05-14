# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

# getting input from user
grade1 = float(input('Primeira nota escolar: '))
grade2 = float(input('Segunda nota escolar: '))

average = (grade1 + grade2) / 2

# printing the result
print('A média das duas notas é \033[4;36m{:.1f}\033[m'.format(average))
