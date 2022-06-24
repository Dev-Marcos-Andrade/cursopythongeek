num = int(input('Digite um número positivo: '))
if num > 0:
    print('Os divisores são: ')
    for i in range(1, num+1):
        if num % i == 0:
            print(i)
else:
    print('O número deve ser positivo!!')
