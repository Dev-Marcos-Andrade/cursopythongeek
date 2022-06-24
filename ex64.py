salário = int(input('Digite seu salárioa: R$'))
tempo = int(input('Digite seu tempo de serviço: '))
if salário <= 500 and tempo == 1:
    reajuste = salário * (25/100)
    tot = salário + reajuste
    print(f'Você um reajuste de 25% seu salário novo é R${tot:.2f} ', end='')
    print('Você não tem bônus ')
elif salário > 500 and salário <= 1000 and tempo > 1 and tempo <= 3:
    reajuste = salário * (20/100)
    tot = salário + reajuste + 100
    print(f'Você um reajuste de 20% seu salário novo é R$ {tot:.2f} ', end='')
    print('mas  um  bônus de R$ 100')
elif salário > 1000 and salário <= 1500 and tempo > 4 and tempo <= 6:
    reajuste = salário * (15/100)
    tot = salário + reajuste + 200
    print(f'Você um reajuste de 15% seu salário novo é R$ {tot:.2f} ', end='')
    print('mas  um  bônus de R$ 200')
elif salário > 1500 and salário < 2000 and tempo > 7 and tempo < 10:
    reajuste = salário * (10/100)
    tot = salário + reajuste + 300
    print(f'Você um reajuste de 10% seu salário novo é R$ {tot:.2f} ', end='')
    print('mas  um  bônus de R$ 300')
elif salário >= 2000 and tempo >= 10:
    tot = salário + 500
    print(f'Você não tem reajuste tem um bônus de R$ 500 seu salário novo é de R${tot:.2f} ')
