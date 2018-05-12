A,G,D=0,0,0
while True:
    x= int(input())
    if x ==1:
        A+=1
    elif x ==2:
        G+=1
    elif x ==3:
        D+=1
    elif x==4:
        break
print('''MUITO OBRIGADO
Alcool: {}
Gasolina: {}
Diesel: {}'''.format(A,G,D))
