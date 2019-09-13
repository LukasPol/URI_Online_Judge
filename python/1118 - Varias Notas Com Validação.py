import sys
def repete():
    print('novo calculo (1-sim 2-nao)')
    y=input()
    if y!='1' and y!='2':
        repete()
    elif y =='2':
        sys.exit()
while True:
    val,s = 0,0
    while True:
        x=float(input())
        if x>=0 and x<=10:
            val+=1
            s+=x
        else:
            print('nota invalida')
        if val == 2:
            break
    print('media = {:.2f}'.format(s/2))
    repete()

