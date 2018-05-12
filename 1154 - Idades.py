q,s=0,0
N = int(input())
while N>=0:
    s+=N
    q+=1
    N = int(input())
print('{:.2f}'.format(s/q))
