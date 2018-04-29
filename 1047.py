n = input().split(' ')
hi = int(n[0])
mi = int(n[1])
hf = int(n[2])
mf = int(n[3])
I = (hi*60)+mi
F = hf*60 + mf
if I >= F:
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format( ((1440 - I) + F)//60,((1440 - I) + F)%60   ))
else:
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format((F - I)//60, (F - I)%60  ))

'''
    428
    
    550

    122//60
    122%60
    '''
