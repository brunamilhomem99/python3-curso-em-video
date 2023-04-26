# Crie um algoritmo que leia um número e mostre seu dobro, seu triplo e a raiz quadrada

# biblioteca para operações aritméticas
import math

# pegando o input do usuário
value = int(input('Digite um valor inteiro: '))

# calculando o dobro do valor
dobro = value * 2

# calculando o triplo do valor
triplo = value * 3

# calculando a raiz quadrada
raiz = math.sqrt(value)

# imprimindo o resultado
print(f'O dobro é valor dado é {dobro}, o triplo é {triplo}, e a raíz quadrada é {raiz}')
