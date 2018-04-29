lista =input().split(' ')
A = int(lista[0])
B = int(lista[1])
C = int(lista[2])
if A<B and A<C:
    if B<C:
        print('{}\n{}\n{}\n\n{}\n{}\n{}'.format(A,B,C,A,B,C))
    else:
        print('{}\n{}\n{}\n\n{}\n{}\n{}'.format(A,C,B,A,B,C))
if B<A and B<C:
    if A<C:
        print('{}\n{}\n{}\n\n{}\n{}\n{}'.format(B,A,C,A,B,C))
    else:
        print('{}\n{}\n{}\n\n{}\n{}\n{}'.format(B,C,A,A,B,C))
if C<B and C<A:
    if A<B:
        print('{}\n{}\n{}\n\n{}\n{}\n{}'.format(C,A,B,A,B,C))
    else:
        print('{}\n{}\n{}\n\n{}\n{}\n{}'.format(C,B,A,A,B,C))

