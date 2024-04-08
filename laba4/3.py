N=int(input("Введите количество городов: "))
SP=[' ']
while N>0:
    gor=input("Введите название города: ")
    if gor not in SP:
        SP.append(gor)
        print("Город принят!")

    else:
        print("Такой город уже есть!")
        N=N+1
    N=N-1