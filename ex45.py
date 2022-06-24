import math
n = int(input('Digite um número: '))
if n < 0:
    print('Número invalido...')
else:
    l = math.log(n, 2)
print(f'O logaritmo de {n} é {l:.2f}')
