# Faça um programa que leia o nome completo de uma pessoa, e mostre o primeiro e o último nome separadamenete;
# ex: input: Ana Maria de Souza. Output: primeiro = Ana, segundo = Maria

n = str(input('Digite seu nome completo: ')).strip()
split = n.split()
print('Primeiro nome: {}\nSegundo nome: {}'.format(split[0], split[len(split)-1]))
