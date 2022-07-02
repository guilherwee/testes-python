from time import sleep
a=int(input('Digíte um número: '))
b=int(input('Digíte mais um número: '))
c=int(input('Digíte mais outro número: '))
menor=a
maior=a
sleep(1)
print('Calculando...')
sleep(1)
if b<a and b<c:
    menor=b
if c<a and c<b:
    menor=c

if b>a and b>c:
    maior=b
if c>a and c>b:
    maior=c
print(f'O número maior é {maior}')
sleep(1)
print(f'O número menor é {menor}')
sleep(1)