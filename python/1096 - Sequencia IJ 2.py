I=0
J=1
for i in range(11):
    if i == 10:
        for z in range (3):
            print('I=2 J=?')
        break        
    for z in range(3):
        if I == 0 or I == 1:
            I=int(I)
            J=int(J)
            print('I={} J={}'.format(I,J))
        else:
            print('I={:.1f} J={:.1f}'.format(I,J))
        J=J+1
    I+=0.2
    J=1+I
    
