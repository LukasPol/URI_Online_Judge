s=0
x=input().split(' ')
A=int(x[0])
if int(x[1])<=0:
    x=input().split(' ')
    N=int(x[1])
else:
    N=int(x[1])
for i in range(N):
    s+=A+i
print(s)
