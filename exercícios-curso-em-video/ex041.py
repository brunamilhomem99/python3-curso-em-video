# A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade.
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 25 anos: SÊNIOR
# Acima: Master

from datetime import date
ano = date.today().year
nasc = int(input('Qual o seu ano de nascimento? '))
idade = ano - nasc
if idade <= 9:
    print('\033[1mCategoria de atletismo:\033[m \033[35mMIRÍM\033[m')
elif idade <= 14:
    print('\033[1mCategoria de atletismo:\033[m \033[35mINFANTIL\033[m')
elif idade <= 19:
    print('\033[1mCategoria de atletismo:\033[m \033[35mJUNIOR\033[m')
elif idade <= 25:
    print('\033[1mCategoria de altetismo:\033[m \033[35mSÊNIOR\033[m')
else:
    print('\033[1mCategoria de atletismo:\033[m \033[35mMASTER\033[m')
