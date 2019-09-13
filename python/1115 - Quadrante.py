while True:
    n=input().split(' ')
    X=int(n[0])
    Y=int(n[1])
    if X==0 or Y ==0:
        break
    elif X>0 and Y>0:
        print('primeiro')
    elif X>0 and Y<0:
        print('quarto')
    elif X<0 and Y>0:
        print('segundo')
    elif X<0 and Y<0:
        print('terceiro')
    

