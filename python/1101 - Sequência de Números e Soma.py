while True:
    s=0
    a=input().split(' ')
    M=int(min(a))
    N=int(max(a))
    if M <=0 or N <=0:
        break
    for z in range(M,N+1):
        s+=z
        print(z,end=' ')
    print('Sum={}'.format(s))

    
