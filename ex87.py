num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
soma_par = 0
multi_impar = 1
if num1 >= num2:
    for i in range(num2, num1+1):
        if i % 2 == 0:
            soma_par += i
        elif i % 2 == 1:
            multi_impar *= i
        elif i % 2 == -1 and i < 0:
            multi_impar *= i
        else:
            print('erro')
elif num2 > num1:
    for i in range(num1, num2+1):
        if i % 2 == 0:
            soma_par += i
        elif i % 2 == 1:
            multi_impar *= i
        elif i % 2 == -1 and i < 0:
            multi_impar *= i
        else:
            print('erro!!')
print(f"A soma dos números pares no intervalo dos números: {soma_par}")
print(f"A multiplicação dos números ímpares no intervalo\n dos números digitados:{multi_impar}")