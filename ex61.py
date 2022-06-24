preço = float(input('Digite o preço: R$ '))
if preço <= 50:
    p = preço * (5/100)
    r = preço + p
    r <= 80
    print(f'O antigo preço era R$ {preço} ', end='')
    print(f'Com o aumento de 5% foi para R$ {r} está barato.')
elif preço >= 50 and preço <= 100:
    p = preço * (10/100)
    r = preço + p
    r > 80 and r <= 120
    print(f'O antigo preço era R$ {preço}', end='')
    print(f'Com o aumento de 10% foi para R$ {r} está normal.')
elif preço > 100 and preço <= 200:
    p = preço * (15/100)
    r = preço + p
    r > 120 and r <= 200
    print(f'O antigo preço era R$ {preço} ', end='')
    print(f'Com o aumento de 15% foi para R$ {r} está caro.')
else:
    print(f'O preço é R$ {preço} está muito caro.')
