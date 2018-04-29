N = []

x = int(input())
N.append(x)

for i in range (10):
    N.append(N[i]*2)
    print('N[{}] = {}'.format(i, N[i]))
