def serpin_t(n):
    tr= [['*']]

    for i in range(n):
        for j in range(len(tr[i])):
            tr[i].append(tr[i][j] + tr[i][j])

        row = []
        for j in range(len(tr[i])):
            row.append(' ' * (2 ** (n - 1 - i)) + tr[i][j] + ' ' * (2 ** (n - 1 - i)))
        tr.append(row)

    for row in tr:
        print(''.join(row))

print("Введите количество: " )
n = int(input())
if (n>2):  # количество итераций (минимум 3)
    serpin_t(n)
