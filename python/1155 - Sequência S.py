P,S=2,1
for i in range(3,40,2):
    S+=i/P
    P*=2
print('{:.2f}'.format(S))
