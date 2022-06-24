from random import randint
n = int(input('Digite quantas vezes quer jogar os dados: '))
d1 = 0
d2 = 0
for i in range(n):
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    print(f'Lançamento {i+1}:')

    if d1 > d2:
        print(f'Dado 1 Foi {d1}')
        print(f'Dado 2 Foi {d2}')
        print(f'Dado 1 Maior que  Dado 2')
    elif d1 < d2:
        print(f'Dado 1 Foi {d1}')
        print(f'Dado 2 Foi {d2}')
        print('Dado 1 Menor que Dado 2')
    else:
        print(f'Dado 1 {d1}')
        print(f'Dado 2 {d2}')
        print('Dado 1 Igual ao  Dado 2')
