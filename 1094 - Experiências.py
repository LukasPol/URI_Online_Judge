N = int(input())
C,R,S=0,0 ,0
for i in range(N):
    a = input().split(' ')
    if a[1].lower()== 'c':
        C+=int(a[0])
    elif a[1].lower() == 'r':
        R+=int(a[0])
    elif a[1].lower() == 's':
        S+=int(a[0])
T=C+S+R
print('''Total: {} cobaias
Total de coelhos: {}
Total de ratos: {}
Total de sapos: {}
Percentual de coelhos: {:.2f} %
Percentual de ratos: {:.2f} %
Percentual de sapos: {:.2f} %'''
      .format( T,C,R,S , (100*C/T), (100*R/T),
               (100*S/T) ))
