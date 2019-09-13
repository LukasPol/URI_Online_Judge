
T = int(input())
for i in range(T):
    F=[0,1]
    N = int(input())
    if N >1:
        for z in range(N):
            F.append(F[z]+F[z+1])
    print('Fib({}) = {}'.format(N, F[N]))
    del F[:]

# 0 1 1 2 3 5 8 13

# 0 1 2 3 4 5 6 7

# 0 1 1 2 3 5 


