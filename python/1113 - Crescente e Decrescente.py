while True:
    A=input().split(' ')
    X = int(A[0])
    Y = int(A[1])
    if X==Y:
        break
    elif X<Y:
        print('Crescente')
    else:
        print('Decrescente')
