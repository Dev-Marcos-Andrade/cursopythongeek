idade = int(input('Digite a idade do nadador: '))
if idade >=5 and idade <=7:
    print(f'Essa idade {idade} esta na classe infantil A.')
elif idade >=8 and idade <= 10:
    print(f'Essa idade {idade} esta na classe infantil B.')
elif idade >= 11 and idade <= 13:
    print(f'Essa idade {idade} esta na classe juvenil A.')
elif idade >= 13 and idade <= 17:
    print(f'Essa idade {idade} esta na classe juvenil B.')
else:
    idade >= 18
    print(f'Essa idade {idade} esta na classe adulta.')
