n = int(input('Digite um número inteiro e positivo: '))
e = 1
if n > 0:
    for i in range(1, n+1):
        f = i
        for j in range(1, f):
            f *= j
        e += 1/f
    print(f'O valor de E é {e:.2f}')
else:
    print('O valor deve ser positivo!!')
