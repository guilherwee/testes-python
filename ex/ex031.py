distancia=float(input('Qual a distancia da viagem em KM? '))
t = 200
if distancia <= t:
    v = distancia * 0.50
    print(f'O valor da passagem será de R${v:.2f}')
else:  
    v = distancia * 0.45
    print(f'O valor da passagem será de R${v:.2f}')