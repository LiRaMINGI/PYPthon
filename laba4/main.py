A = input("Введите числа через пробел: ")
b=A.split()
CH=set()
for i in b:
    CH.add(int(i))
print(len(CH))
