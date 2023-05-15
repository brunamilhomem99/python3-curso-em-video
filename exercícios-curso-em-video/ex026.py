# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra 'A';
# Em que posição ela aparece a primeira vez;
# Em que posição ela aparece a última vez;

f = str(input('Digite um frase: ')).upper()
count = f.count('A')
string = f.replace(" ", "")    # tirando os espaços para que só as letras sejam levadas em conta
find = string.find('A')+1
rfind = string.rfind('A')+1
print(f'A letra A aparece \033[31m{count}\033[m vezes, aparece pela primeira vez na posição de índice \033[31m{find}\033[m e aparece pela última vez na posição \033[31m{rfind}\033[m')
