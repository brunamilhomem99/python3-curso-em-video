# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
# o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o flag)

qtd_num = {}
c = 1
while c == 1:
    n = int(input('Digite um número inteiro: '))
    if n == 999:
        if n in qtd_num:
            qtd_num[n] += 1
        else:
            qtd_num[n] = 1
        break
print(qtd_num)
