for i in range(999, 100, -1):
    p = ''
    for j in range(i, 100, -1):
        p = str(i  * j)
        if p[::1] == p[::-1]:
            break
    if p[::1] == p[::-1]:
        print(f'{p} = {i} * {j}')
        break