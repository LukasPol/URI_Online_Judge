N=int(input())
X=[]
x=input().split(' ')
for i in range(N):
    X.append(int(x[i]))
print('''Menor valor: {}
Posicao: {}'''.format(min(X), X.index(min(X))))
