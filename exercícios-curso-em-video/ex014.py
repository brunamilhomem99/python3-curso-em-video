# Escreva um programa que leia a temperatura em graus Celcius (Cº) e converta para Fahrenheit (Fº)

cel = float(input('Temperatura em celcius: '))
print('O valor da temperatura em \033[33m{}ºC\033[m equivale a \033[36m{:.2f}ºF\033[m'.format(cel, cel * 1.8 + 32))
