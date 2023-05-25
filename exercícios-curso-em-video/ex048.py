# Faça um programa que calcule a soma entre todos os números ímpares
# que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
cont = 0
print('\033[34mNúmeros ímpares múltiplos de 3:\033[m')
for n in range(1, 501, 2):
    if n % 3 == 0:
        cont += 1
        soma += n
print(f'A soma de todos os \033[31m{cont}\033[m valores solicitados é: \033[31m{soma}\033[m')
