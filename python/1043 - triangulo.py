lista = input().split(' ')
A = float(lista[0])
B = float(lista[1])
C = float(lista[2])
if A < B + C and B < A + C and C < B + A:
    print('Perimetro = {:.1f}'.format(A+B+C))
else:
    print('Area = {:.1f}'.format( ((A+B)*C)/2 ))
    
