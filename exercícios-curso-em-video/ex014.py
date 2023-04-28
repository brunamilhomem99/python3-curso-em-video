# Escreva um programa que leia a temperatura em graus Celcius (Cº) e converta para Fahrenheit (Fº)

cel = float(input('Temperatura em celcius: '))
print('O valor da temperatura em {}ºC equivale a {:.2f}ºF'.format(cel, cel * 1.8 + 32))
