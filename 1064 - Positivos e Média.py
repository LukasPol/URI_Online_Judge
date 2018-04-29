p = 0
m = 0
for i in range (6):
    n = float(input())
    if n >= 0 :
        m+=n
        p+=1
print('{} valores positivos\n{:.1f}'.format(p,m/p))
