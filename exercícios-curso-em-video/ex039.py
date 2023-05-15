# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar;
# Se é a hora de se alistar;
# Se já passou do tempo de alistamento;
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
nasc = int(input('\033[1;30mQual o seu ano de nascimento? \033[m'))
ano = date.today().year
idade = ano - nasc
if idade < 18:
    saldo = 18 - idade
    print(f'Você ainda não chegou a maioridade. Ainda faltam \033[34m{saldo}\033[m anos para o alistamento.')
    ano = ano + saldo
    print(f'Você irá alistar-se em \033[34m{ano}\033[m')
elif idade > 18:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há \033[34m{saldo}\033[m anos!')
    ano = ano - saldo
    print(f'Você se alistou em \033[34m{ano}\033[m')
elif idade == 18:
    print('Parabéns! Você chegou a maioridade e agora já deverá se alistar \033[31mIMEDIATAMENTE\033[m. Boa sorte!')
