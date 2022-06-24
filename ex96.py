t = 10
c1 = 0
c2 = 0
c3 = 0
for i in range(1, t+1):
    c1 += i
    if i == t:

        if i % 2 == 0:
            c2 += -i + (2 * t - 1)

        elif i % 2 == 1:
            c2 += i + (2 * t - 1)
            c3 += i

        c3 += (2 * t - 1)
        break

    if i % 2 == 0:
        c2 -= i

    elif i % 2 == 1:
        c2 += i
        c3 += i
print(c1)
print(c2)
print(c3)