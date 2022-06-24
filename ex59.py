altura = float(input('Digite a altura: '))
peso = float(input('Digite o peso: '))
if altura < 1.20 and peso <= 60:
    print('A classificação é A')
elif altura >= 1.20 and altura <= 1.70 and peso <= 60:
    print('A classificação é B')
elif altura > 1.70 and peso <= 60:
    print('A classificação é C')
elif altura < 1.20 and peso > 60 and peso <= 90:
    print('A classificação é D')
elif altura >= 1.20 and altura <= 1.70 and peso > 60 and peso <= 90:
    print('A classificação é E')
elif altura > 1.70 and peso > 60 and peso <= 90:
    print('A classificação é F')
elif altura < 1.20 and peso > 90:
    print('A classificação é G')
elif altura >= 1.20 and altura <= 1.70 and peso > 90:
    print('A classificação é H')
elif altura > 1.70 and peso > 90:
    print('A classificação é I')


