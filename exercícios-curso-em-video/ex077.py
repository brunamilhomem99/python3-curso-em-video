# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

purple = '\033[35m'
cyan = '\033[36m'
reset = '\033[m'

palavras = ('Estrela', 'Quasar', 'Nebulosa', 'Exoplaneta', 'Gravidade', 'Luz', 'Poeira')
for p in palavras:
    print(f'\nA palavra {purple}{p}{reset} possui: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{cyan}{letra}{reset}', end=' ')
        