N = int(input())
for i in range (N):
    nt = input().split(' ')
    a = float(nt[0])
    b = float(nt[1])
    c = float(nt[2])
    print('{:.1f}'.format( (a*2 + b*3 + c*5)/10))
