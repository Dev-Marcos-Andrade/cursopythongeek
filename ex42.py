s = float(input('Digite o seu salario: R$'))
p = float(input('Digite o valor do empréstimo: R$'))
mínimo = s * 20 / 100
if p <= mínimo:
    print('Empréstimo aprovado')
else:
    print('Empréstimo negado!!')
