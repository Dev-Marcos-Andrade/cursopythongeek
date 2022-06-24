n = 50
soma_par = 0
cont = 0
for i in range(1, 100):
    if i % 2 == 0:
        print(i)
        soma_par += 1
        cont += 1
    if cont >= 50:
        break
print(soma_par)
