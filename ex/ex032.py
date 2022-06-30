import time
print('Vou identificar se o ano é bissexto ou não.')
time.sleep(1)
ano=int(input('Digite o ano: '))
if (ano%400==0):
    print('Este ano é bissexto.')
else:
    print('Este ano não é bissesto.')