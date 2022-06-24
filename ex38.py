import math
num = int(input('Digite um número: '))
if num >= 0:
    riaz = math.sqrt(num)
    q = num * num
    print(f'O número {num} ao quadrado é {q}')
    print(f'A raiz do número {num} é {riaz}')
else:
    print('Esse número é invalido')
