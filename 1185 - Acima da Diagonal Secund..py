T,S = [] ,0
op = input()
for i in range(12):
    A =[]
    for j in range(12):
        A.append(float(input()))
    T =T +[A]    
for i in range(12):
    for j in range(12):
        if i + j <= 10:
            S = S + T[i][j]
if op.lower() =='s':
    print('{:.1f}'.format(S))
else:
    print('{:.1f}'.format(S/66))
