valor = float(input('Digite um valor do produto: R$'))
estado = str(input('Digite o estado: ')).strip().upper()
if estado == 'MG':
    p = valor * (7/100)
    res = p + valor
    print(f'O valor final do produto é de {res:.2f}')
elif estado == 'SP':
    p = valor * (12 / 100)
    res = p + valor
    print(f'O valor final do produto é de {res:.2f}')
elif estado == 'RJ':
    p = valor * (15 / 100)
    res = p + valor
    print(f'O valor final do produto é de {res:.2f}')
elif estado == 'MS':
    p = valor * (8 / 100)
    res = p + valor
    print(f'O valor final do produto é de {res:.2f}')
else:
    estado != 'MG', 'SP', 'RJ', 'MS',
    print('Estado invalido... ')
