# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
from math import cos, sin, tan, radians
ang = int(input('Digite o valor um ângulo qualquer: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('Seno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(sen, cos, tan))