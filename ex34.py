print('<<< ASSISTENTE DE VENDAS >>>')
print('-='*30)
v = float(input('Digite o valor da venda: R$'))
tot = v * (10/100)
t = v - tot
print(f'O valor a ser pago com desconto de 10% é R${t}')
print('-='*30)
val = v / 3
print(f'O valor da parcela 3x sem juros é R${val:.2f}')
print('-='*30)
com = t * (5/100)
print(f'A comissão do vendedor caso a venda seja a vista é de 5% R${com}')
print('-='*30)
totv = v * (5/100)
print(f'A comissão do vendedor parcelada é de 5% do valor total R${totv}')
print('<<< FIM... >>>')