def f(S):
    words = S.split()
    ABB = ""
    for w in words:
        ABB += w[0].upper()
    return ABB

S = input("Введите строку: ")
res = f(S)
print("Аббревиатура:", res)