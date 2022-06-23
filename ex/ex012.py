p = float(input('Qual é o preço do produto? R$'))
per = (p*5)/100
calc = p-per
print(f'O valor R${p:.2f} com 5% de desconto fica: R${calc:.2f}')
