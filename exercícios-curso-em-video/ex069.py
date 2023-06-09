# Crie um programa que leia a idade e o gênero de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o user quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos;
# B) quantos homens foram cadastrados;
# C) quantas mulheres tem menos de 20 anos;
# D) quantas pessoas não binárias foram cadastradas. [BÔNUS]

from time import sleep

maioridade = homens = mulheres20 = nao_binario = 0
while True:
    idade = int(input('Idade: '))

    gen = ' '
    while gen not in 'FMNB':
        gen = str(input('Gênero [F / M / NB]: ')).strip().upper()

    if idade >= 18:
        maioridade += 1
    if gen == 'M':
        homens += 1
    if gen == 'F' and idade < 20:
        mulheres20 += 1
    if gen == 'NB':
        nao_binario += 1

    opc_continuar = ' '
    while opc_continuar not in 'SN':
        opc_continuar = str(input('Quer continuar [S / N]? ')).strip().upper()[0]
    if opc_continuar == 'N':
        break

print('COLETANDO ESTATÍSTICA. . .')
sleep(2)

print(f'Total de pessoas com mais de de 18 anos: {maioridade}')
print(f'Total de homens cadastrados: {homens}')
print(f'Total de mulheres com menos de 20 anos: {mulheres20}')
print(f'Total de pessoas não binárias: {nao_binario}')
