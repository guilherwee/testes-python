n = int(input('Digite um número com quatro dígitos: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'milhar: {m}')
print(f'centena: {c}')
print(f'dezena: {d}')
print(f'unidade: {u}')
