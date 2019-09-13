A=[0,1]
N=int(input())
if N == 1:
    del A[1:]
else:
    for i in range(N-2):
        A.append(A[i]+A[i+1])
for i in A:
    if i== A[-1]:
        print(i)
    else:
        print(i,end=(' '))
