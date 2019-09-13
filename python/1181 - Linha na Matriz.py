M =[]
N = int(input())
op = input()
for i in range(5):
    A = []
    for j in range(5):
        A.append(float(input('{}X{}'.format(i,j))))
    M.append(A)
for j in range(12):
    S =sum(M[N])
if op.lower() == 's':
    print('{:.1f}'.format(S))
else:
    print('{:.1f}'.format(S/12))
