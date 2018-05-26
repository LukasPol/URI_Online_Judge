N=[]
X = float(input())
while len(N) <= 5:
    N.append(X)
    X = X/2
for i in range(100):
    print('N[{}] = {:.4f}'.format(i,N[i]))
