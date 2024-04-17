def SP(X):
    A = []
    for l in X:
        A.append(l.split())
    return A

def STR(M):
    SS=''
    for a in M:
        SS=SS+a+' '
    return SS

with open("input2.txt", "r", encoding="utf-8") as f:
    S = f.readlines()
    f.close()
    
K = len(S)
NS = SP(S)
for i in range(K):
    for j in range(K):
        if int(NS[i][2]) > int(NS[j][2]):
            T = NS[j]
            NS[j] = NS[i]
            NS[i] = T


F1=open("output2.txt",'w')
F1.write(STR(NS[0]))
F1.close()

F2=open("output3.txt",'w')
F2.write(STR(NS[-1]))
F2.close()
