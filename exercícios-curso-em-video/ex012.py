# Faça um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

price = float(input('Digite o preço do produto: R$'))
new_price = price - (price * 5 / 100)
print(f'O valor deste produto com desconto de 5% é R${new_price}')
