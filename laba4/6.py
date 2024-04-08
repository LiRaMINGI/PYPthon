a= input() # водим строку через пробель
b=a.split()

g=''# это вывод
m=[]# слова 1 шт
n=[]# масив в котром работаем
for i in range(len(b)):
    if b[i]not in m:
        m.append(b[i])
        e=[]
        e.append(b[i])
        c=0
        for y in range(len (b)):
            if b[i]==b[y]:
                c+=1
        e.append(c)# [слово, число сколько раз оно в тексте]
        n.append(e)# [[e],[e1],.....[en]]

e=len(n)
for i in range(e-1):
    for j in range(e-i-1):
        if n[j][1]<n[j+1][1]:
            n[j], n[j+1]= n[j+1], n[j]
        elif n[j][1]==n[j+1][1]:
            c = n[j][0]
            c1 = n[j + 1][0]
            if len(c)<len(c1):
                z=len(c1)-len(c)
                for t in range(z):
                    c=c+' '
            elif len(c)>len(c1):
                z=len(c)-len(c1)
                for t in range(z):
                    c1=c1+' '
            for y in range(len(n[j][0])):
                if c[y]==' ' and c1[y]!=' ':
                    break
                elif c[y]!=' ' and c1[y]==' ':
                    n[j], n[j + 1] = n[j + 1], n[j]
                    break
                elif ord(c[y])<ord(c1[y]):
                    n[j], n[j + 1] = n[j + 1], n[j]
                    break
for i in range(len(n)):
    g=n[i][0]+" "
    print(g)
