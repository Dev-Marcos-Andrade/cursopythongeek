print('   CALCULE A ÁREA DE UM TRAPÉZIO   ')
basemaior = int(input('Digite a basemaior do trapézio: '))
basemenor = int(input('Digite a basemenor do trapézio: '))
altura = int(input('Digite a altura do trapézio: '))
res = (basemaior + basemenor) * altura / 2
if basemaior and basemenor > 0:
    print(f'A área do trapézio é {res}')
else:
    print('ERRO!! A base maior é a base menor tem que ser maior que 0')
