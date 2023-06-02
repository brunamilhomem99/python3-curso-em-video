# escreva um programa que leia um número n inteiro qualquer e mostre
# na tela os n primeiros elementos de uma Sequência de Fibonacci.
# ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

red = '\033[31m'
blue = '\033[34m'
reset = '\033[m'

from time import sleep
termos = int(input('Quantos termos você quer que apareça? '))
print(f'{red}GERANDO SEQUÊNCIA DE FIBONACCI...{reset}')
sleep(2)
t1 = 0
t2 = 1
print(f'{t1} - {t2} - ', end='')
c = 3
while c <= termos:
    t3 = t1 + t2
    print(f'{t3} - ', end='')
    t1 = t2
    t2 = t3
    c += 1
print(f'{blue}FIM{reset}')