nota = 0
soma = 0
cont = 0
while True:
    nota = float(input('Digite uma nota entre 10 e 20: '))
    if (nota >= 10) and (nota <= 20):
        soma += nota
        cont += 1
    else:
        if cont == 0:
            cont += 1
        print(f'Nota {nota} invalida!!')
        break
print('Média aritmética: %.1f (excluindo a última nota digitada)' % (soma / cont))
