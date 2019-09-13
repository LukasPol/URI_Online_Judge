P,I=[],[]
for i in range(15):
    X = int (input())
    if X%2 == 0:
        P.append(X)
        if len(P)==5:
            for z in range(5):
                print('par[{}] = {}'.format(z,P[z]))
            del P[:]
    else:
        I.append(X)
        if len(I) == 5:
            for z in range(5):
                print('impar[{}] = {}'.format(z,I[z]))
            del I[:]
X=len(I)
for z in range(X):
    print('impar[{}] = {}'.format(z,I[z]))
X=len(P)
for z in range(X):
    print('par[{}] = {}'.format(z,P[z]))
            
