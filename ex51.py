a = int(input('Primeiro segmento: '))
b = int(input('Segundo segmento: '))
c = int(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima podem forma um triangulo.')
    print('-' * 50)
    if a == b == c:
        print('Equilátero.')
    elif a != b != c != a:
        print('Escaleno.')
    else:
        print('Isósceles')
else:
    print('Os segmentos acima não podem forma um triangulo.')
