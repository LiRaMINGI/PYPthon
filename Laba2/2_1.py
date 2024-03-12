def f(n):
    tr= []
    for i in range(n):
        r = []
        for j in range(i + 1):
            if j == 0 or j == i:
                r.append(1)
            else:
                r.append(tr[i - 1][j - 1] + tr[i - 1][j])
        tr.append(r)

    for r in tr:
        print(' '.join(map(str, r)))


n = int(input("Введите число строк: "))
f(n)
