
N = int(input())

for i in range(N):
    A=[]
    X = int(input())
    for j in range(1,X):
        if X % j == 0:
            A.append(j)
    s = sum(A)
    if s == X:
        print('{} eh perfeito'.format(X))
    else:
        print('{} nao eh perfeito'.format(X))
    
            
    
