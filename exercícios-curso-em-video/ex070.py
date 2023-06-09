# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o user vai continuar. No final, mostre:
# A) qual é o total gasto na compra;
# B) quantos produtos custam mais de R$1000,00;
# C) qual é o nome do produto mais barato.

from time import sleep
total_gasto = protudos1000 = mais_barato = cont = 0
mais_barato_nome = ' '
while True:
    nome_produto = str(input('Nome do produto: '))
    valor_produto = float(input('Valor do produto: R$'))
    cont += 1

    opc_continuar = ' '
    while opc_continuar not in 'SN':
        opc_continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]

    total_gasto += valor_produto
    if valor_produto > 1000:
        protudos1000 += 1
    if cont == 1 or valor_produto < mais_barato:
        mais_barato = valor_produto
        mais_barato_nome = nome_produto

    if opc_continuar == 'N':
        break
print('CALCULANDO...')
sleep(2)
print(f'Total gasto na compra: R${total_gasto:.2f}')
print(f'Total de produtos que custam mais de R$1000,00: {protudos1000}')
print(f'Produto mais barato: {mais_barato_nome}, custando R${mais_barato}')