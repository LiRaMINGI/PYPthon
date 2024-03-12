def count(S):
    SP = {}
    for i in S:
        if i in SP:
            SP[i] += 1
        else:
            SP[i] = 1
    for i in SP.values():
        print(i, end=' ')

A = ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc']
count(A)  # вывод: 3 1 2 1

B = ['aaa', 'bbb', 'ccc']
count(B)  # вывод: 1 1 1

C = ['abc', 'abc', 'abc']
count(C)  # вывод: 3