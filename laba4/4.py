"""
a=input("Введите строку: ")
b=a.split()
g=''
e=''
for i in range(len(b)):
    e=e+' '+str(g.count(b[i]))
    print (e)
    g=g+' '+ b[i]
    print(g)
print(e)

"""
A = input("Введите строку: ")
b=A.split()
k=''
STR=''
for i in range(len(b)):
    k = k+ ' ' + str(STR.count(b[i]))
    STR = STR + b[i]
print(k)
