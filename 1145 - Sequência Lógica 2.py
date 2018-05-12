a=input().split(' ')
X=int(a[0])
Y=int(a[1])
for i in range(1,Y+1):
    if i%X==0:
        print(i)
    else:
        print(i,end=(' '))
