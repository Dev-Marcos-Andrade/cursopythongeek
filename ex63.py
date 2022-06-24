venda = float(input('Digite o valor da venda: R$'))
if venda >= 10000000:
    p = venda * (16 / 100)
    tot = 700 + p
    print(f'O valor da venda foi R$ {venda:.2f} ', end='')
    print(f'A comissão do vendedor é R$ {tot:.2f}')
elif venda < 10000000 and venda >= 80000000:
    p = venda * (14 / 100)
    tot = 650 + p
    print(f'O valor da venda foi R$ {venda:.2f} ', end='')
    print(f'A comissão do vendedor é R$ {tot:.2f}')
elif venda < 80000000 and venda >= 60000000:
    p = venda * (14 / 100)
    tot = 600 + p
    print(f'O valor da venda foi R$ {venda:.2f} ', end='')
    print(f'A comissão do vendedor é R$ {tot:.2f}')
elif venda < 60000000 and venda >= 40000000:
    p = venda * (14 / 100)
    tot = 550 + p
    print(f'O valor da venda foi R$ {venda:.2f} ', end='')
    print(f'A comissão do vendedor é R$ {tot:.2f}')
elif venda < 40000000 and venda >= 20000000:
    p = venda * (14 / 100)
    tot = 500 + p
    print(f'O valor da venda foi R$ {venda:.2f} ', end='')
    print(f'A comissão do vendedor é R$ {tot:.2f}')
elif venda < 20000000:
    p = venda * (14 / 100)
    tot = 400 + p
    print(f'O valor da venda foi R$ {venda:.2f} ', end='')
    print(f'A comissão do vendedor é R$ {tot:.2f}')




