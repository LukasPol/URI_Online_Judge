L1 = input().split(' ')
A = int(L1[0])
B = int(L1[1])
C = int(L1[2])
D = int(L1[3])
if A%2 ==0 and B>C and D>A and (C+D) > (A+B) and (C and D) > 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
