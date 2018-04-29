s = float(input())
if s<=2000:
    print('Isento')
elif s>2000 and s<=3000:
    print('R$ {:.2f}'.format(s*0.08))
elif s>3000 and s<=4500:
    print('R$ {:.2f}'.format(s*0.18))
elif s>4500:
    print('R$ {:.2f}'.format(s*0.28 ))
