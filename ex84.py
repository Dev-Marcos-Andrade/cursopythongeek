n = int(input('Digite a quantidade de números a ser lida: '))
maior = 0
for i in range(1, n+1):
    num = int(input(f'Digite o {i}º números: '))
    if i == 1:
        num = maior
    elif num > maior:
        maior = num
print(f'O maior número é {maior}')
