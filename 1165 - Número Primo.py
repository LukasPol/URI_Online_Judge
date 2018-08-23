N = int(input())

for i in range(N):
    A=True
    X = int(input())
    for j in range(2,X):
        if X%j == 0:
            A = False
            break
    if A == False:
        print('{} nao eh primo'.format(X))
    else:
        print('{} eh primo'.format(X))


