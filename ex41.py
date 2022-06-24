n1 = float(input('Digite a nota1: '))
n2 = float(input('Digite a nota2: '))
if n1 < 0:
    print(f'Nota {n1} invalida ')
elif n2 < 0:
    print(f'Nota {n2} invalida ')
elif n1 > 10:
    print(f'Nota {n1} invalida ')
elif n2 > 10:
    print(f'Nota {n2} invalida')
else:
    resp = n1 + n2 / 2
    print(f'O aluno com as notas {n1} e {n2} tem a media {resp}')
