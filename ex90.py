num = int(input('Digite um número: '))
soma = 0
if num > 0:
    for i in range(1, num):
        if num % i == 0:
            soma += i
    print(f'A soma dos divisores do {num} é {soma}')
elif num < 0:
    for i in range(num+1, 0, 1):
        if num % i == 0:
            print(i)
            soma += i
    print(f"A soma dos divisores do número {num} é {soma}")

