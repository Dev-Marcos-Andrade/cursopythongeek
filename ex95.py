t = 5
s = 0
f = 1
for i in range(1, t+1):
    f = 2 * i
    for j in range(1, f):
        f *= j
    s += i/f
print(f'O valor da série é {s:.2f}')