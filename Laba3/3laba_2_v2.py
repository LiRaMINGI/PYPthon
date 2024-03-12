def f(S):
    SL=""  #Будущая строчка
    c='0123456789'
    NS=S+'**'
    Z=[]; A=[]

    for n in range(len(NS)):  #В цикле проставляю одиночным буквам цифру 1
        if NS[n].isalpha() and NS[n+1].isalpha():
            NS=NS.replace(NS[n],NS[n]+'1',1)

    AS=NS[:-2]

    for i in range(len(NS)):  #Заменяю все буквы на #
        if NS[i] not in c:
            NS=NS.replace(NS[i],'#',1)

    N = NS.split('#') #Убираю #

    for d in N: #Закидываю цифры в массив
        if d!='':
            Z.append(int(d))

    for j in range(len(AS)):  #Заменяю все цифры на ?
        if AS[j] in c:
            AS = AS.replace(AS[j], '?', 1)

    SS = AS.split('?') #Убираю ?

    for b in SS: #Закидываю в массив
        if b!='':
            A.append(b)

    if len(A) == len(Z): #Если кол-во букв и цифр совпадают, то ок
        for m in range(len(A)):
            SL+=A[m]*Z[m]
        return SL
    else:
        return "Error"

S = str(input("Введите строку: "))
print(S)
print (f(S))
#Y4g2ke3A3BV
