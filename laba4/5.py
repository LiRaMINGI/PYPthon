N = int(input("Кол-во записей о покупках: "))
SP=[]
for i in range(N):
    S=input("ID, Товар, Кол-во: ")
    SP.append(S.split())

#b=[]

#for i in range(len(a)):
#    if q in a[i][0] :
#        b.append(a[i][1])
#        b.append(a[i][2])
#print(b)

for i in range(len(SP)):
    STR = ''
    q=SP[i][0]
    print(q)
    for x in range (len(SP)):
        for y in range(len(SP[i])-2):
            if q in SP[x][y]:
                STR = STR + SP[x][y+1] + " "+ SP[x][y+2]+ '     '
                SP[x][y]=''
                SP[x][y+1] = ''
                SP[x][y+2] = ''
    print(STR)