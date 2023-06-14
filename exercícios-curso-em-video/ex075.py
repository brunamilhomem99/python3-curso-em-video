# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9;
# B) Em que posição foi digitado o primeiro valor 3;
# C) Quais foram os números pares.

user_value = (int(input('Digite um número: ')), int(input('Digite mais um número: ')), int(input('Mais um: ')), int(input('O último: ')))

print(f'Você digitou os números {user_value}')

if 9 in user_value:
    print(f'Quantidade de ocorrências do número 9: {user_value.count(9)}')
else:
    print('O valor 9 não foi digitado em nenhuma posição.')

if 3 in user_value:
    print(f'índice da primeira ocorrência do valor 3: {user_value.index(3) + 1}')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')

print('Valores pares digitados:', end=' ')
for i in user_value:
    if i % 2 == 0:
        print(i, end=' ')
