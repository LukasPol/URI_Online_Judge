lista =input().split(' ')
A = int(lista[0])
B = int(lista[1])
C = int(lista[2])

if A>B and A>C:
    print('{} eh o maior'.format(A))
elif B>A and B>C:
    print('{} eh o maior'.format(B))
elif C>A and C>B:
    print('{} eh o maior'.format(C))

