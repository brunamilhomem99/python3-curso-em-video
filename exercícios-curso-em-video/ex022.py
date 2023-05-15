# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas;
# O nome com todas as letras minúsculas;
# quantas letras o nome contém (sem considerar espaços);
# Quantas letras tem o primeiro nome;

nome = str(input('Digite seu nome completo: '))
no_space = nome.replace(" ", "")
first_name = nome.split()
print(f'Em maiúsculo: \033[35m{nome.upper()}\033[m\nEm minúsculo: \033[36m{nome.lower()}\033[m\nPossui \033[34m{len(no_space)}\033[m letras\n'
      f'Possui \033[31m{len(first_name[0])}\033[m letras no primeiro nome')