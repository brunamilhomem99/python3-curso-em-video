# Desenvolva um programa que leia o comprimento de três retas e diga ao user se elas podem ou não formar um triângulo.

print('\033[35m-=-' * 20)   # testando o sistema de coloração do terminal
print('\033[1;30;46mAnalisador de triângulos...\033[m')
print('\033[35m-=-\033[m' * 20)
r1 = float(input('Primeiro valor de reta: '))
r2 = float(input('Segundo valor de reta: '))
r3 = float(input('Terceiro valor de reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'\033[32mCom os comprimentos dados é possível fazer um triângulo com perímetro de {r1 + r2 + r3}cm!')
else:
    print(f'\033[31mOs comprimentos dados não são suficientes para formar um triângulo.')
