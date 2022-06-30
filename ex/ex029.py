vel=float(input('Quantos km por hora você está? '))
m = (vel-80)*7
if vel > 80:
    print(f'Você foi multado em R${m:.2f}')
else:
    print('Ok, você não foi multado.')