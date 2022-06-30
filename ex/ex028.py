import random
from time import sleep
print('Computador: vou escolher um número de 0 a 5 e você tem que advinhar qual é este número.')
n1=int(input('Vamos lá! digite um número: '))
comp = random.randint(0,5)
print('Calculando...')
sleep(3)
if n1 == comp:
    print('Parabéns, você acertou!')
else:
    print(f'Que pena, você errou! era o número {comp}.')