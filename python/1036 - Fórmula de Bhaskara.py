L1 = input().split(' ')
A = float(L1[0])
B = float(L1[1])
C = float(L1[2])
D = (B**2) - (4*A*C)

if A == 0 or D<0:
    print('Impossivel calcular')
else:
    R1 = ( -B + (D)**(1/2) ) / (2*A)
    R2 = ( -B - (D)**(1/2) ) / (2*A)
    print('''R1 = {:.5f}
R2 = {:.5f}'''.format(R1, R2))
