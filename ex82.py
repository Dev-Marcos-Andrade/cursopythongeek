num = int(input('Digite um número impar e positivo: '))
if num > 0 and num % 2 == 1:
    for i in range(num+1, -1, -1):
        if i % 2 == 1:
            print(i)
else:
    print('O número digitado não é impar ou positivo!!!')
