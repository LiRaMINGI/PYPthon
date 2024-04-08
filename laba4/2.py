Z1= input("Введите первое множество: ")
Z=Z1.split()
G1= input("Введите второе множество: ")
G=G1.split()
fl = True
if len(Z)<len(G) :
    for i in range(len(Z)):
        if Z[i] not in G:
            fl =False
            break
else:
    fl =False
print(fl)