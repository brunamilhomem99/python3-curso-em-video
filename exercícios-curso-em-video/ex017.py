# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo,
# calcule e mostre o comprimento da hiponetusa
from math import pow, sqrt
cat_oposto = float(input('Digite o valor do cateto oposto do triângulo: '))
cat_adj = float(input('Agora do cateto adjacente: '))
hip = sqrt(pow(cat_oposto, 2) + pow(cat_adj, 2))
print('O valor da Hipotenusa é {:.2f}'.format(hip))
