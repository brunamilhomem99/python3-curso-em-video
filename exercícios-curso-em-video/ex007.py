# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

# getting input from user
grade1 = float(input('Digite o valor de uma nota escolar: '))
grade2 = float(input('Digite outro: '))

average = (grade1 + grade2) / 2

# printing the result
print('A média das duas notas é {:.1f}'.format(average))
