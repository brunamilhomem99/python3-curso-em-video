# A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade.
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 20 anos: SÊNIOR
# Acima: Master

import datetime
nascimento = int(input('Qual o seu ano de nascimento? '))
ano = datetime.datetime.now().year
if ano - nascimento < 9:
    print('\033[1mCategoria de atletismo:\033[m \033[35mMIRÍM\033[m')
elif ano - nascimento < 14:
    print('\033[1mCategoria de atletismo:\033[m \033[35mINFANTIL\033[m')
elif ano - nascimento < 19:
    print('\033[1mCategoria de atletismo:\033[m \033[35mJUNIOR\033[m')
elif ano - nascimento < 20:
    print('\033[1mCategoria de altetismo:\033[m \033[35mSÊNIOR\033[m')
elif ano - nascimento > 20:
    print('\033[1mCategoria de atletismo:\033[m \033[35mMASTER\033[m')
