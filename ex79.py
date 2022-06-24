num = int(input('Digite um número positivo e par: '))
if num % 2 == 0:
    for i in range(1, num+1):
        if i % 2 == 0:
            print(i)
else:
    print('O número digitado não é par ou é negativo!!')