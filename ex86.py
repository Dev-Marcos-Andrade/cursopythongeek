num = 0
conte_número = 0
conte_par = 0
while num != 1000:
    num = int(input('Digite um número: '))
    if (num > 0) and (num % 2 == 0) or (num < 0 ) and (num % 2 == -1):
        conte_par += 1
    conte_número += 1
print(f'Os números lidos foi {conte_número}')
print(f'Os números pares foi {conte_par}')