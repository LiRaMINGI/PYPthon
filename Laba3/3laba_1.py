def f(S):
    SL=""
    for i in S:
        if i not in SL:
            d=S.count(i)
            if d==1:
                SL=SL+i
            else:
                SL=SL+i+str(d)
    return SL
                

S = str(input("Введите строку: " ))
print(S)
print (f(S))
#Y4g2ke3A3BV
#YYYYggkeeeAAABV