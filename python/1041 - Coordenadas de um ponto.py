lista = input().split(' ')
X = float(lista[0])
Y = float(lista[1])
if X==0 and Y==0:
    print('Origem')
elif X ==0:
    print('Eixo Y')
elif Y ==0:
    print('Eixo X')
elif X > 0 and Y > 0:
    print('Q1')
elif X > 0 and Y < 0:
    print('Q4')
elif X < 0 and Y > 0:
    print('Q2')
elif X < 0 and Y < 0:
    print('Q3')
