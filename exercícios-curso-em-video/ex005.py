# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

# getting input from user
value = int(input('Digite um número inteiro: '))

# printing the result
print(f'O \033[1msucessor\033[m é \033[31m{value+1}\033[m e o \033[1mantecessor\033[m é \033[31m{value-1}\033[m')
