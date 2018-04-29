for i in range(100):
    x = float(input())
    A.append(x)
for z in range (len(A)):
    if A[z] <= 10:
        print('A[{}] = {}'.format(z, A[z]))
