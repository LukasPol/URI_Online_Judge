N =[]
n = input().split(' ')
for i in range(3):
    N.append(float(n[i]))
N.sort()
A = N[2]
B = N[1]
C = N[0]
if A >= B+C:
    print('NAO FORMA TRIANGULO')
else:
    if A**2 == B**2 + C**2:
        print('TRIANGULO RETANGULO')
    if A**2 > B**2 + C**2:
        print('TRIANGULO OBTUSANGULO')
    elif A**2 < B**2 + C**2:
        print('TRIANGULO ACUTANGULO')
    if A==B and A==C:
        print('TRIANGULO EQUILATERO')
    elif A==B or B==C:
        print('TRIANGULO ISOSCELES')

