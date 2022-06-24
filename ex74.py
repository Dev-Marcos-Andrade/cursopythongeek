maior = menor = 0
for n in range(1, 11):
    num = int(input(f"{n}º número: "))
    if n == 1:
        maior = menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
print(f'O número maior é:{maior}')
print(f'O número menor é: {menor}')