# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9;
# B) Em que posição foi digitado o primeiro valor 3;
# C) Quais foram os números pares.

step_array = []
tupla = ''
user_value = 0
for i in range(1, 5):
    user_value = int(input(f'Valor {i}: '))
    step_array.append(user_value)
    tupla = tuple(step_array)
print(tupla)
print(f'Quantidade de ocorrências do número 9: {tupla.count(9)}')
position = tupla.index(3)
print(f'índice da primeira ocorrência do valor 3: {position}')
print('Valores pares digitados:', end=' ')
for i in tupla:
    if i % 2 == 0:
        print(i, end=' ')
