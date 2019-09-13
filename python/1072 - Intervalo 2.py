d=0
f=0
N = int(input())
for i in range(N):
    X = int(input())
    if X>=10 and X<=20:
        d +=1
    else:
        f +=1
print('{} in\n{} out'.format(d,f))
