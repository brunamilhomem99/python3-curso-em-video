# Faça um programa que leia o nome completo de uma pessoa, e mostre o primeiro e o último nome separadamenete;
# ex: input: Ana Maria de Souza. Output: primeiro = Ana, segundo = Maria

n = str(input('Digite seu nome completo: '))
split = n.split()
print(f'Primeiro nome: {split[0]}\nNome do meio: {split[1]}\nÙltimo nome: {split[2]}')
