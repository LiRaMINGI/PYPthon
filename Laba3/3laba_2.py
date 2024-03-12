def f(S):
    SL=""
    Ch = len(S)
    c='0123456789'
    NS=S+'*'
    AS=S+'*'
    Z=[]; A=[]

    for i in range(len(NS)):
        if NS[i] not in c:
            NS=NS.replace(NS[i],'#',1)
    for z in range (len(NS)-1):
        if NS[z] == '#':
            if NS[z]=='#' and NS[z+1]!='#':
                Z.append(int(NS[z+1]))
            #if NS[z]=='#' and NS[z+1]!='#':
                #Z.append(int(NS[z+1]))
            elif NS[z]=='#' and NS[z+1]=='#':
                Z.append(1)

    for j in range(len(AS)):
        if AS[j] in c:
            AS = AS.replace(AS[j], '?', 1)

    for a in range (len(AS)-1):
        if AS[a] != '?':
            if AS[a]!='?' and AS[z+1]=='?':
                A.append(AS[a])
            elif AS[a]!='?' and AS[z+1]!='?':
                A.append(AS[a])
    #for k in range(len()):
    print(NS, '',Z,'', AS, A)
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