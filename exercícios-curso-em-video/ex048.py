# Faça um programa que calcule a soma entre todos os números ímpares
# que são múltiplos de três e que se encontram no intervalo de 1 até 500.

print('\033[34mNúmeros ímpares múltiplos de 3:\033[m')
for n in range(1, 500, 2):
    if n % 3 == 0:
        print(n)
