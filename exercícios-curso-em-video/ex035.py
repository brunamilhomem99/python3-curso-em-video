# Desenvolva um programa que leia o comprimento de três retas e diga ao user se elas podem ou não formar um triângulo.

print('\033[35m-=-' * 20)
print('\033[36mAnalisador de triângulos...\033[m')
print('\033[35m-=-\033[m' * 20)
r1 = float(input('\033[32mPrimeiro valor de reta:\033[m '))
r2 = float(input('\033[33mSegundo valor de reta:\033[m '))
r3 = float(input('\033[34mTerceiro valor de reta:\033[m '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'Com os comprimentos dados é possível fazer um triângulo com perímetro \033[32m{r1 + r2 + r3}cm!\033[m')
else:
    print(f'\033[31mOs comprimentos dados não são suficientes para formar um triângulo.\033[m')
