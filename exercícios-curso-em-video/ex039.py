# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar
# Se já passou do tempo de alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime
nascimento = int(input('\033[1;37mQual o seu ano de nascimento? \033[m'))
ano = datetime.datetime.now().year
if ano - nascimento < 18:
    print('Você ainda não chegou a maioridade, portanto o alistamento militar ainda não é obrigatório.')
elif ano - nascimento > 18:
    print('Você já possui mais de 18 anos, logo, já deveria ter se alistado no exéricito!')
elif ano - nascimento == 18:
    print('Parabéns! Você chegou a maioridade e agora já deve se alistar no serviço militar, Boa sorte!')
