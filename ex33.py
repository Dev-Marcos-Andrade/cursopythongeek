h = int(input('Digite quantas horas por mês você trabalha: '))
s = h * 5.51
p = s * (10/100)
tot = s + p
print(f'As horas mensais foram {h}')
print(f'O valor do salario foi R${s:.2f} com 10% ficou R${tot:.2f}')
