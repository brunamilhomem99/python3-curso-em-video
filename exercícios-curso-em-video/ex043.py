# Desenvolva uma lógica que leia o peso e altura de uma pessoa,
# calcule seu IMC e mostre seu status de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do Peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida

p = float(input('Qual é o seu peso? (Kg) '))
a = float(input('Qual é a sua altura? (m) '))
imc = p / (a ** 2)
if imc < 18.5:
    print('\033[31mAbaixo do peso\033[m')
    print(imc)
elif 18.5 <= imc < 25:
    print('\033[32mPeso ideal\033[m')
elif 25 <= imc < 30:
    print('\033[34mSobrepeso\033[m')
elif 30 <= imc <= 40:
    print('\033[35mObesidade\033[m')
elif imc > 40:
    print('\033[31mObesidade mórbida\033[m')
