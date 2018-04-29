n = input().split(' ')
A = float(n[0])
B = float(n[1])
C = float(n[2])
for i in range(len(n)):
    if A < float(n[i]):
        A = float(n[i])
    elif C >= float(n[i]):
        C = float(n[i])
    else:
        B = float(n[i])
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

