# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o 999,
# que é a CONDIÇÃO DE PARADA (FLAG), foi digitada. No final,  mostre quantos números foram digitados e
# qual foi a soma entre eles. (desconsiderando a flag).

purple = '\033[35m'
cyan = '\033[36m'
reset = '\033[m'

cont = num = soma = 0
while True:
    num = int(input('Digite um número inteiro [999 para parar]: '))
    
    if num != 999:
        cont += 1
        soma += num
    else:
        break

print(f'Foram lidos {purple}{cont}{reset} números e a soma entre eles foi {cyan}{soma}{reset}')
