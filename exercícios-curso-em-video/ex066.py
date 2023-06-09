# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o 999,
# que é a CONDIÇÃO DE PARADA (FLAG), foi digitada. No final,  mostre quantos números foram digitados e
# qual foi a soma entre eles. (desconsiderando a flag).

cont = num = soma = 0
while True:
    num = int(input('Digite um número inteiro [999 para parar]: '))
    if num != 999:
        cont += 1
        soma += num
    else:
        break
print(f'Foram lidos {cont} números e a soma entre eles foi {soma}')
