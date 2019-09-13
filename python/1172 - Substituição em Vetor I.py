X=[]

for i in range(10):
    n = int(input())
    if n <= 0 :
        n = 1
    X.append(n)

for z in range(10):
    print('X[{}] = {}'.format(z, X[z]))
    
