dias = int(input('Dias alugados: '))
km = int(input('KMs percorridos: '))
pago = dias*60 + (km*0.15)
print(f'{km}KMs percorridos em {dias} dias, equivale à R${pago}')
