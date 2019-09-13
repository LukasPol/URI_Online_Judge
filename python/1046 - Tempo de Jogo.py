n = input().split(' ')
hi = int(n[0])
hf = int(n[1])
if hi >= hf:
    print('O JOGO DUROU {} HORA(S)'.format((24 - hi) + hf))
else:
    print('O JOGO DUROU {} HORA(S)'.format(hf - hi))
'''    
hf -hi

(24 - hi) + hf
'''
