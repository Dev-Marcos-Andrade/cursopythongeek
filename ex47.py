dia = int(input('Digite um dia da semana: '))
if dia == 1:
    print(f'O {dia} dia corresponde a o domingo.')
elif dia == 2:
    print(f'O {dia} dia correponde a segunda-feira')
elif dia == 3:
    print(f'O {3} dia corresponde a terça-feira. ')
elif dia == 4:
    print(f'O {dia} dia correponde a quarta-feira.')
elif dia == 5:
    print(f'O {dia} dia correponde a quinta-feira.')
elif dia == 6:
    print(f'O {dia} dia corresponde a sexta-feira.')
elif dia == 7:
    print(f'O {dia} dia correponde a sábado.')
else:
    dia = (0, 7)
    print('ERRO esse dia da semana não existe.')
