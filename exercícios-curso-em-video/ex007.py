# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

# getting input from user
grade1 = int(input('Digite o valor de uma nota escolar: '))
grade2 = int(input('Digite outro: '))

# summing up the values
grade_sum = grade1 + grade2

# dividing the result by the input length
average = grade_sum / 2

# printing the result
print('A média das duas notas é', average)
