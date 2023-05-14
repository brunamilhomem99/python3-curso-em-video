# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo,
# calcule e mostre o comprimento da hiponetusa
from math import hypot
cat_oposto = float(input('Digite o valor do cateto oposto do triângulo: '))
cat_adj = float(input('Agora do cateto adjacente: '))
hip = hypot(cat_oposto, cat_adj)
print('O valor da Hipotenusa é \033[31m{:.2f}\033[m'.format(hip))
