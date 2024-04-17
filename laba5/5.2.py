f=open("input1.txt")
S=f.read()
SA=S.split('\n')
SA.sort()
f.close()
F=open("output1.txt",'w')
for i in SA:
    F.write(i+'\n')
F.close()