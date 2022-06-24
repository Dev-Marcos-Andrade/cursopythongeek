n = int(input('Digite o valor de N: '))
if n > 0:
    v1 = int(input('Digite o primeiro valor: '))
    v2 = int(input('Digite o segundo valor: '))

    if v1 > 0 and v2 > 0:
        lista = []

        for i in range(n):
            if not (v1 * i in lista):
                lista.append(v1 * i)

            if not (v2 * i in lista):
                lista.append(v2 * i)
        lista.sort()
        for i in range(n):
            print(lista[i])
    else:
        print('Os números não podem ser zero ou negativo!!!')
else:
    print('O valor de N não pode ser zero ou negativo!!!')
