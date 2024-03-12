def f(S):
    SL=""  #Будущая строчка
    c='0123456789'
    NS=S+'**'
    Z=[]; A=[]

    for n in range(len(NS)):
        if NS[n] not in c and NS[n+1] not in c:
            NS=NS.replace(NS[n],NS[n]+'1',1)
    AS=NS[:-2]
    for i in range(len(NS)):
        if NS[i] not in c:
            NS=NS.replace(NS[i],'#',1)
    N = NS.split('#')
    for d in N:
        if d!='':
            Z.append(int(d))

    for j in range(len(AS)):
        if AS[j] in c:
            AS = AS.replace(AS[j], '?', 1)

    SS = AS.split('?')
    for b in SS:
        if b!='':
            A.append(b)

    if len(A) == len(Z):
        for m in range(len(A)):
            SL+=A[m]*Z[m]
        return SL
    else:
        return "Error"

S = str(input("Введите строку: "))
print(S)
print (f(S))
#Y4g2ke3A3BV
