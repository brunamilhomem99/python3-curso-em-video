# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('Estrela', 'Quasar', 'Nebulosa', 'Exoplaneta', 'Gravidade', 'Luz', 'Poeira')
for i in palavras:
    if i in 'aeiou':
        print(i)
        