n = int(input('Digite um número entre 100 e 999: '))
if (n >= 100) and (n <= 999):
    lista = str(n)
    print('Os algarismo que compõem o número:')
    for x, y in enumerate(lista):
        print(y, end='  ')
print('O número digitado deve esta entre 100 e 999.')


