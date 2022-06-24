print('<<< Escolha a Opção: >>>')
print('1 - Soma de 2 números.\n'
      '2 - Diferença entre 2 números.\n'
      '3 - Produto entre 2 números.\n'
      '4 - Divisão entre 2 números.')
print('~' * 40)
opc = int(input('Digite sua opção: '))
print('~' * 40)
if opc == 1:
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite segundo número: '))
    res = num1 + num2
    print('~' * 40)
    print(f'A soma dos números {num1} e {num2} é {res}')
elif opc == 2:
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite segundo número: '))
    if num1 > num2:
        print(f'O maior número entre  {num1} e {num2} é {num1}')
    elif num2 > num1:
        print(f'O maior número entre  {num1} e {num2} é {num2}')
    else:
        print('Os números são iguais..')
elif opc == 3:
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite segundo número: '))
    res = num1 * num2
    print(f'O produto dos números {num1} e {num2} é {res}')
elif opc == 4:
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite segundo número: '))
    if num1 and num2 != 0:
        res = num1 / num2
        print(f'A divisão entre os números {num1} e {num2} é {res}')
    else:
        print('ERRO!!! número 0 invalido...')
else:
    opc = (1, 5)
    print('Opção invalida...')






