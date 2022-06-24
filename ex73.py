num = 0
for _ in range(10):
    valor = int(input('Digite um número: '))
    if valor > 0:
        num = num + valor
        média = num / 10
print(f'A média do números positivos é {média}')
