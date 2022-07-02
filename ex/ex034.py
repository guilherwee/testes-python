salário = float(input('Digite o seu salário aqui R$:'))
#print(f'R${salário}')
if salário > 1250:
    cal=salário + (salário * 10/100)
if salário <=1250:
    cal=salário + (salário * 15/100)
print(f'O seu salário foi aumentado para: R${cal:.2f}')