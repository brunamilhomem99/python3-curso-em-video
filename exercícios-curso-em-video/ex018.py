# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
from math import cos, sin, tan
ang = int(input('Digite o valor um ângulo qualquer: '))
print(f'Seno: {cos(ang)} \n Cosseno: {sin(ang)} \n Tangente: {tan(ang)}')
