print('  Operações matemáticas  ')
print('-' * 40)
print(' 1 - Soma de dois valores.\n'
      ' 2 - Subtração de dois valores.\n'
      ' 3 - Multiplicação de dois valores.\n'
      ' 4 - Divisão de dois valores.')
print('-' * 40)
opc = int(input('Digite sua opção: '))
if opc == 1:
    v1 = float(input('Digite o primeiro valor: '))
    v2 = float(input('Digite o segundo valor: '))
    res = v1 + v2
    print('-' * 40)
    print(f'A soma dos valores {v1} e {v2} é {res:.1f}')
elif opc == 2:
    v1 = float(input('Digite o primeiro valor: '))
    v2 = float(input('Digite o segundo valor: '))
    res = v1 - v2
    print('-' * 40)
    print(f'A subtração dos valores {v1} e {v2} é {res:.1f}')
elif opc == 3:
    v1 = float(input('Digite o primeiro valor: '))
    v2 = float(input('Digite o segundo valor: '))
    res = v1 * v2
    print('-' * 40)
    print(f'A multiplicação dos valores {v1} e {v2} é {res:.1f}')
else:
    opc == 4
    v1 = float(input('Digite o primeiro valor: '))
    v2 = float(input('Digite o segundo valor: '))
    res = v1 / v2
    print('-' * 40)
    print(f'A divisão dos valores {v1} e {v2} é {res:.1f}')
print('-' * 40)
print('Volte sempre....')

