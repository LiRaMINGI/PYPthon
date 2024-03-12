def f(a, b, c):
    if a <= b and a <= c:
        MIN = a
    elif b <= a and b <= c:
        MIN = b
    else:
        MIN = c
        
    if a >= b and a >= c:
        MAX = a
    elif b >= a and b >= c:
        MAX = b
    else:
        MAX = c
        
    return MIN, MAX


A = float(input("Введите первое число: "))
B = float(input("Введите второе число: "))
C = float(input("Введите третье число: "))

MINZ, MAXZ = f(A, B, C)

print("Минимальное число:", MINZ)
print("Максимальное число:", MAXZ)
