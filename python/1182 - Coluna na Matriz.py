M = []
S = 0
N = int(input())
op = input()
for i in range(12):
    A = []
    for j in range(12):
        A.append(float(input()))
    M.append(A)
for i in range(12):
    for j in range(12):
        if j == N:
            S += M[i][j]
if op.lower() == 's':
    print('{:.1f}'.format(S))
else:
    print('{:.1f}'.format(S/12))
