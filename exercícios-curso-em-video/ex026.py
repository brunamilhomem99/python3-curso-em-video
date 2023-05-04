# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra 'A';
# Em que posição ela aparece a primeira vez;
# Em que posição ela aparece a última vez;

f = str(input('Digite um frase: ')).upper()
count = f.count('A')
string = f.replace(" ", "")    # tirando os espaços para que só as letras sejam levadas em conta
find = string.find('A')+1
rfind = string.rfind('A')+1
print(f'A letra A aparece {count} vezes, aparece pela primeira vez na posição de índice {find} e aparece pela última vez na poisção {rfind}')
