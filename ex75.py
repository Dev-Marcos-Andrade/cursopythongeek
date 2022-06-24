num = int(input("Digite o valor de n: "))
soma_impar = 0
cont = 0
for i in range(1, num*num):
    if i % 2 == 1:
        print(i)
        cont += 1
    if cont >= num:
        break