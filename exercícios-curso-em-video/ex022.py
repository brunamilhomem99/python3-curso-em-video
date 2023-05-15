# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas;
# O nome com todas as letras minúsculas;
# quantas letras o nome contém (sem considerar espaços);
# Quantas letras tem o primeiro nome;

nome = str(input('Digite seu nome completo: '))
no_space = nome.replace(" ", "")
first_name = nome.split()
print(f'\033[35mEm maiúsculo: {nome.upper()}\033[m\n\033[36mEm minúsculo: {nome.lower()}\033[m\n\033[\033[34mPossui {len(no_space)} letras\033[m\n'
      f'\033[31mPossui {len(first_name[0])} letras no primeiro nome\033[m')