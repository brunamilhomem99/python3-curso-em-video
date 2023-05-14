# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

value = int(input('Digite um valor em \033[4mmetros\033[m: '))

# printing the result
print(f'O valor \033[34m{value}\033[m em centímetros é \033[31m{value*100}\033[m e em milímetros é \033[32m{value*1000}\033[m')
