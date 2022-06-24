num = int(input('Digite um número positivo e par: '))
if (num > 0) and (num % 2 == 0):
    for i in range(num+1, -1, -1):
        if i % 2 == 0:
            print(i)
else:
    print('O número digitado não é par ou positivo!!!')


