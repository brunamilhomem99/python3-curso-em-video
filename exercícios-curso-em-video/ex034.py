# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# para salários superiores a R$1.250,00, calcule um aumento de 10%
# para os inferiores ou iguais, o aumento é de 15%.

s = float(input('Qual o valor do seu salário? R$'))
superior = s + (s * 10/100)
inferior = s + (s * 15/100)
if s > 1250:
    print('Considerando o valor dado você terá um aumento de \033[4m10%\033[m, passando a receber \033[32mR${:.2f}\033[m'.format(superior))
elif s <= 1250:
    print('Considerando o valor dado você terá um aumento de \033[4m15%\033[m, passando a receber \033[32mR${:.2f}\033[m.'.format(inferior))
