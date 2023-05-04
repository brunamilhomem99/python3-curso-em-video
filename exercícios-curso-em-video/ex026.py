# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra 'A';
# Em que posição ela aparece a primeira vez;
# Em que posição ela aparece a última vez;

f = str(input('Digite um frase: '))
count = f.count('a')
string = f.replace(" ", "")    # tirando os espaços para que só as letras sejam levadas em conta
find = string.find('a')
rfind = string.rfind('a')
print(f'A letra A aparece {count} vezes, aparece pela primeira vez na posição de índice {find} '
      f'e aparece pela última vez na poisção {rfind}')
