# Faça um programa que leia o nome completo de uma pessoa, e mostre o primeiro e o último nome separadamenete;
# ex: input: Ana Maria de Souza. Output: primeiro = Ana, segundo = Maria

n = str(input('\033[36mDigite seu nome completo: \033[m')).strip()
split = n.split()
print('Primeiro nome: \033[1m{}\033[m\nSegundo nome: \033[1m{}\033[m'.format(split[0], split[len(split)-1]))
