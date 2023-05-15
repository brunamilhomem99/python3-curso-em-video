# Escreva um programa que leia dois número inteiros e compare-os, mostrando na tela uma mensagem:
# 0 primeiro valor é maior
# 0 segundo valor é menor
# Não existe valor maior. Os dois são iguais.

a = int(input('\033[1;37mPrimeiro valor: \033[m'))
b = int(input('\033[1;37mSegunddo valor: \033[m'))
if a > b:
    print('O primeiro valor é \033[4;40mmaior\033[m.')
    print('O segundo valor é \033[4;40mmenor\033[m.')
elif b > a:
    print('O segundo valor é \033[4;40mmaior\033[m.')
    print('O primeiro valor é \033[4;40mmenor\033[m. ')
elif a == b:
    print('Os dois valores são \033[4;40miguais\033[m.')
