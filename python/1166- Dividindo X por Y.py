N=int(input())
for i in range (N):
    n = input().split(' ')
    x=int(n[0])
    y=int(n[1])
    if y ==0:
        print('divisao impossivel')
    else:
        print('{}'.format(x/y))
