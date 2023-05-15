# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de converção:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

n = int(input('\033[1;37mEscolha um número inteiro qualquer: \033[m'))
b = int(input('\033[1;37mEscolha uma base de converção entre Binário (1), Octal (2) ou Hexadecimal (3): \033[m'))

# convertendo as bases de acordo com o input do usuário
if b == 1:
    print('O número \033[32m{}\033[m é equivalente a \033[33m{}\033[m em \033[4mBinário\033[m.'.format(n, bin(n)[2:]))
elif b == 2:
    print('O número \033[32m{}\033[m é equivalente a \033[35m{}\033[m em \033[4mOctal\033[m.'.format(n, oct(n)[2:]))
elif b == 3:
    print('O número \033[32m{}\033[m é equivalente a \033[36m{}\033[m em \033[4mHexadecinaml\033[m.'.format(n,
                                                                                                            hex(n)[2:]))
