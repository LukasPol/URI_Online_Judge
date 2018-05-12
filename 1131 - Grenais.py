import sys
def repete():
    print('Novo grenal (1-sim 2-nao)')
    y=input()
    if y!='1' and y!='2':
        repete()
    elif y =='2':
        print('''{} grenais
Inter:{}
Gremio:{}
Empates:{}'''.format(grenais,I,G,E))
        if I>G:
            print('Inter venceu mais')
        elif G>I:
            print('Gremio venceu mais')
        elif G==I:
            print('Nao houve vencedor')
        sys.exit()
I,G,E,grenais = 0,0,0,0
while True:
    x=input().split(' ')
    A=int(x[0])
    B=int(x[1])
    grenais+=1
    if A>B:
        I+=1
    elif B>A:
        G+=1
    elif A==B:
        E+=1
    repete()
