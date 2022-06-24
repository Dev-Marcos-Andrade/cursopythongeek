a = float(input('Digite sua altura: '))
s = str(input('Qual o seu sexo [M/F]: ')).strip().upper()
h = 72.7 * a - 58
m = 62.1 * a - 44.7
if s == 'Mm':
    print(f'O seu peso ideal é {h}.')
elif s == 'Ff':
    print(f'Seu peso ideal é {m}')
