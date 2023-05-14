# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar

money = float(input('Quantos reais você tem na carteira? R$'))

# cotação do dolar
print(f'Com \033[32mR${money}\033[m você pode comprar \033[32mUS${money*5}\033[m dólares!')
