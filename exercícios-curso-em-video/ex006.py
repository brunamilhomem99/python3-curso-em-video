# Crie um algoritmo que leia um número e mostre seu dobro, seu triplo e a raiz quadrada

# pegando o input do usuário
value = int(input('Digite um valor inteiro: '))

# imprimindo o resultado
print(f'O \033[1mdobro\033[m do valor dado é \033[35m{value*2}\033[m, o \033[1mtriplo\033[m é \033[32m{value*3}\033[m, e a \033[1mraíz quadrada\033[m é \033[36m{value**(1/2)}\033[2m')
