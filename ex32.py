dia = int(input('Digite os dias trabalhados: '))
t = dia * 30
p = t * (8/100)
tot = t - p
print(f'Você trabalhou {dia} dias deu o valor de R${t} com o desconto de 8% fica R${tot}')