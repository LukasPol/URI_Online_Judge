x = int(input())
if x%2!=0:
    for i in range(x,x+11,2):
        print(i)
if x%2==0:
    for i in range(x+1,x+13,2):
        print(i)

