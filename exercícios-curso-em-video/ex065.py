# Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostre a média e qual foi foi o maior e o menor valores lidos. O programa deve perguntar ao user se ele quer ou não continar a digitar os valores.

r = 'S'
soma = quant = avg = maior = menor = 0
while r in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    r = str(input('Quer continuar? [S/N]: ')).strip()[0].upper()
avg = soma / quant
print(f'Você digitou {quant} valores. O maior foi {maior}, o menor foi {menor} e a média entre eles foi {avg}.')



