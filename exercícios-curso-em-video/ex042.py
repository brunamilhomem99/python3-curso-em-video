# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo será formado.
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais
# ESCALENO: todos os lados diferentes

print('\033[35m-=-' * 15)
print('\033[1;36mANALISADOR DE TRIÂNGULOS...\033[m')
print('\033[35m-=-\033[m' * 15)
r1 = float(input('Primeiro valor de reta: '))
r2 = float(input('Segundo valor de reta: '))
r3 = float(input('Terceiro valor de reta: '))
if r1 == r2 == r3:
    print('Triângulo \033[36mEQUILÁTERO\033[m')
elif r1 == r2 or r1 == r3 or r2 == r3:
    print('Triângulo \033[36mISÓCELES\033[m')
elif r1 != r2 != r3:
    print('Triângulo \033[36mESCALENO\033[m')
