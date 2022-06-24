valor = int(input('Valor do carro novo: R$ '))
if valor <= 12000:
    distri = valor * (5/100)
    tot = valor + distri
    print(f'O valor total do carro com os impostos é de R${tot:.1f}')
elif valor > 12000 and valor < 25000:
    distri = valor * (10/100)
    impos = valor * (15/100)
    tot = valor + distri + impos
    print(f'O valor total do carro com os impostos é de R${tot:.1f}')
elif valor > 25000:
    distri = valor * (15/100)
    impos = valor * (20/100)
    tot = valor + distri + impos
    print(f'O valor total do carro com os impostos é de R${tot:.1f}')