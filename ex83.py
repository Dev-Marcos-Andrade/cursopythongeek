num = int(input("Digite um número inteiro e positivo: "))
soma = 0
if num > 0:
    print(f"A soma dos {num} primeiros números naturais:")
    for i in range(1, num*num):
        if i <= num:
            soma += i

        else:
            break

    print(soma)
else:
    print("O número não pode ser zero ou negativo!")