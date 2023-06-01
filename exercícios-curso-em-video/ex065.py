# Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores lidos. O programa deve perguntar ao user se ele
# quer ou não continar a digitar os valores.

num = []
avg = 0
c = 1
while c == 1:
    n = int(input('Digite um número: '))
    num.append(n)
    q = str(input('Quer continuar? [S/N]: ')).upper()
    if len(num) > 2:
        if q == 'N':
            avg = sum(num) / len(num)
            print(f'A média dos valores digitados é {avg:.2f}')
            break
    elif q not in 'SN':
        print('Opção ou valor inálido. Não é possível realizar a operação.')
        break




