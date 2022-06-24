altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
icm = peso / (altura * altura)
if icm <= 18.5:
    print(f'Seu ICM é {icm:.2f} você está abaixo do peso')
elif icm > 18.6 and icm < 24.9:
    print(f'Seu ICM é {icm:.2f} você está saudável ')
elif icm > 25.0 and icm < 29.9:
    print(f'Seu ICM é {icm:.2f} você está com peso em excesso')
elif icm > 30.0 and icm < 34.9:
    print(f'Seu ICM é {icm:.2f} você está com obesidade grau 1')
elif icm > 35.0 and icm < 39.9:
    print(f'Seu ICM é {icm:.2f} você está com obesidade grau 2 (severa)')
else:
    icm > 40.0
    print(f'Seu ICM é {icm:.2f} você está com obesidade grau 3 (mórbida)')
