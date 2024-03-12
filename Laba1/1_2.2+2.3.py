def f(n):
    for i in range(n, 0, -1):
        print(" " * (n-i), end='')
        for j in range(i, 0, -1):
            print(j, end='')
        for k in range(2, i+1):
            print(k, end='')
        print()

n = int(input("Введите натуральное число: "))

f(n)
