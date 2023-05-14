# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e os dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

km = int(input('Km percorridos: '))
d = float(input('Quantidade de dias do aluguel: '))
preço = (d * 60) + (km * 0.15)
print(f'O total do aluguel do carro, levando em conta os \033[30m{km}Km\033[m percorridos será \033[34mR${preço}\033[m')