s = 0
t1 = range(1, 100, 2)
t2 = range(1, 51)
for i in range(1, 50):
    s += t1[i]/t2[i]
print(f'{s:.2f}')