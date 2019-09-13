n = input().split(' ')
A = int(n[0])
B = int(n[1]) 
if B<A:
    t=A
    A=B
    B=t
    if B == A*(B//A):
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')
else:
    if B == A*(B//A):
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')
