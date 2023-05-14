# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
from math import cos, sin, tan, radians
ang = int(input('Digite o valor um ângulo qualquer: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('\033[34mSeno: {:.2f}\033[m\n\033[35mCosseno: {:.2f}\033[m\n\033[36mTangente: {:.2f}\033[m'.format(sen, cos, tan))