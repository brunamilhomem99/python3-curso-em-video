# Faça um algoritmo que leia o salário de um funcionário de e mostre um novo salário com 15% de aumento

salary = float(input('Digite o valor do seu salário atual: R$'))
new_salary = salary + (salary * 15 / 100)
print(f'Com um aumento de 15%, seu salário foi de R${salary} para R${new_salary}!')
