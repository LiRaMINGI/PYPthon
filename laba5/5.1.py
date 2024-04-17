def PR(X):
    D=1
    for i in X:
        D=D*int(i)
    return D

f=open("input.txt")
S=f.readline()
SA=S.split()
f.close()
D=str(PR(SA))
F=open("output.txt",'w')
F.write(D)
F.close()