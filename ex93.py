n = int(input('Digite um número inteiro e positivo: '))
h = 1
if n > 0:
    for i in range(1, n+1):
        h += 1/i
        print(f'O valor de h(n) é {h:.2f}')
else:
    print('O valor deve ser positivo!!!')