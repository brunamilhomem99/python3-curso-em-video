# Faça um programa que leia a largura e a alura de uma parede em metros, calcule a sua área e
# a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta um área de 2m²

altura = float(input('Altura da parede: '))
largura = float(input('Largura da parede: '))

# calculando a area
area = altura * largura

# quantidade delitros necessários para a area calculada
L = area / 2

print(f'Para pintar sua parede de \033[33m{area}m²\033[m serão necessários \033[33m{L} litros\033[m de tinta!')



