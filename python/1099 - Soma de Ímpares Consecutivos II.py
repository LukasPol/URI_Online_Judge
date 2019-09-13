
N = int(input())
for i in range(N):
    s=0
    a=input().split(' ')
    X = int(min(a))
    Y = int(max(a))
    if X%2!=0:
        for i in range(X+2,Y,2):
           s+=i         
    elif X%2==0:
        for i in range(X+1,Y,2):
            s+=i
    print(s)
'''
if X<Y:
    if X%2!=0:
        for i in range(X+2,Y,2):
           s+=i         
    elif Y%2==0:
        for i in range(X+1,Y,2):
            s+=i
elif Y<X:
    if Y%2!=0:
        for i in range(Y+2,X,2):
           s+=i         
    elif Y%2==0:
        for i in range(Y+1,X,2):
            s+=i
            '''

