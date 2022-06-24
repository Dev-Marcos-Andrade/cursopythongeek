print('<<< Cardápio da Lanchonete >>>')
print('Cachorro Quente  Preço R$ 1,20 cod: 100 \n'
      'Bauru Simples preço R$ 1,30 cod: 101 \n'
      'Bauru com Ovo preço R$ 1,50 cod: 102 \n'
      'Hamburguer preço R$ 1,20 cod: 103 \n'
      'Cheeseburguer preço R$ 1,70 cod: 104 \n'
      'Suco preço R$ 2,20 cod: 105 \n'
      'Refrigerante preço R$ 1,00 cod: 106')
print('-' * 30)
código = int(input('Digite o código: '))
q = int(input('Digite a quantidade de lanches: '))
if código == 100:
    res = 1.20 * q
    print('-' * 30)
    print(f'Seu pedido foi {q} cachorro quente o valor total foi R$ {res}')
elif código == 101:
    res = 1.30 * q
    print('-' * 30)
    print(f'Seu pedido foi {q} bauru simples o valor total foi R$ {res}')
elif código == 102:
    res = 1.50 * q
    print('-' * 30)
    print(f'Seu pedido foi {q} bauru com ovo o valor total foi R$ {res}')
elif código == 103:
    res = 1.20 * q
    print('-' * 30)
    print(f'Seu pedido foi {q} hamburguer o valor total foi R$ {res}')
elif código == 104:
    res = 1.70 * q
    print('-' * 30)
    print(f'Seu pedido foi {q} cheeseburguer o valor total foi R$ {res}')
elif código == 105:
    res = 2.20 * q
    print('-' * 30)
    print(f'Seu pedido foi {q} sucos o valor total foi R$ {res}')
elif código == 106:
    res = 1.00 * q
    print('-' * 30)
    print(f'Seu pedido foi {q} refrigerante o valor total foi R$ {res}')
else:
    código == (100, 102, 103, 104, 105, 106)
    print('-' * 30)
    print('Erro código invalido!!!!')