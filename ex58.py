a = float(input('Escreva um número: '))
b = float(input('Escreva um número: '))
c = float(input('Escreva um número: '))
if a <= b and a <= c and b <= c:
    print(f'A ordem crescente é {a} , {b} e {c}')
elif a <= b and a <=c and c <= b:
    print(f'A ordem crescente é {a} , {c} e {b}')
elif b <= a and b <= c and a <= c:
    print(f'A ordem crescente é {b} , {a} e {c}')
elif b <= a and b <= c and c <= a:
    print(f'A ordem crescente é {b} , {c} e {a}')
elif c <= a and c <= b and a <=b:
    print(f'A ordem crescente é {c} , {a} e {b}')
elif c <= a and c <= b and b <= a:
    print(f'A ordem crescente é {c} , {b} e {a}')