# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas;
# O nome com todas as letras minúsculas;
# quantas letras o nome contém (sem considerar espaços);
# Quantas letras tem o primeiro nome;

nome = str(input('Digite seu nome completo: '))
no_space = nome.replace(" ", "")
first_name = nome.split()
print(f'Em maiúsculo: {nome.upper()}\nEm minúsculo: {nome.lower()}\nPossui {len(no_space)} letras\nPossui {len(first_name[0])} letras no primeiro nome')
