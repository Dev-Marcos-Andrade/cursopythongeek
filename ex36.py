import math
num = int(input('Digite um número: '))
if num >= 0:
    resp = math.sqrt(num)
    print(f'A raiz quadrada de {num} é {resp}')
else:
    print(f'Esse número é invalído.')