# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
import emoji
print('\033[1;37m=\033[m' * 35)
print('\033[36mCONTAGEM REGRESSIVA PARA OS FOGOS...\033[m')
print('\033[1;37m=\033[m' * 35)
for fogos in range(10, -1, -1):
    sleep(1)
    print(fogos)
print(emoji.emojize(":fireworks:" * 10), "\033[35mPOW\033[m \033[34mPOW\033[m \033[36mBOOM\033[m \033[32mBOOM\033[m!")