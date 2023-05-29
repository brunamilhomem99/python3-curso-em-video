# Desenvolva um programa que leia o nome, idade e genêro de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo;
# Qual o nome do homem mais velho;
# Quantas mulheres tem menos de 21 anos.

homem_mais_velho = 0
nome_mais_velho = ''
mulher = 0
soma_idades = 0
for p in range(1, 5):
    nome = str(input(f'Nome {p}: ')).strip()
    genero = str(input(f'Gênero {p} [M/F]: ')).strip()
    idade = int(input(f'Idade {p}: '))
    soma_idades += idade
    if genero in 'Mm' and p == 1:
        homem_mais_velho = idade
        nome_mais_velho = nome
    if genero in 'Mm' and idade > homem_mais_velho:
        homem_mais_velho = idade
        nome_mais_velho = nome
    if genero in 'Ff' and idade < 21:
        mulher += 1

avg = soma_idades / 4
print(f'A média das idades do grupo é {avg} anos.')
print(f'O homem mais velho tem {homem_mais_velho} anos e se chama {nome_mais_velho}.')
print(f'{mulher} mulheres tem menos de 21.')
