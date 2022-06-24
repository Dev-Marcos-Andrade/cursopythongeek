import math
num = int(input('Digite um número: '))
if num >= 0:
    resp = math.sqrt(num)
    print(f'A raiz quadrada de {num} é {resp:.2f}')
else:
    r = num * num
    print(f'Esse número {num} ao quadrado é {r}')
