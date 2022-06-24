num = int(input('Digite um número: '))
list = [11, 13, 17]
print(f'O primeiro múltiplo de 11, 13 ou 17 é {num}')
for x, y in enumerate(list):
    print(num * y)
    