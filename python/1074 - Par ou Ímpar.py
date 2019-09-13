N=int(input())
for i in range(N):
    a=int(input())
    if a == 0:
        print('NULL')
    elif a%2 == 0 and a>0:
        print('EVEN POSITIVE')
    elif a%2 == 0 and a<0:
        print('EVEN NEGATIVE')
    elif a%2 != 0 and a>0:
        print('ODD POSITIVE')
    elif a%2 != 0 and a<0:
        print('ODD NEGATIVE')    
