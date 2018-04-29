L1 = input().split(' ')
A = float(L1[0])
B = float(L1[1])
C = float(L1[2])
D = float(L1[3])
M = ( A*2 + B*3 + C*4 + D*1 )/10
if M >=7:
    print('''Media: {:.1f}
Aluno aprovado.'''.format(M))
elif M <5:
    print('''Media: {:.1f}
Aluno reprovado.'''.format(M))
else:
    print('''Media: {:.1f}
Aluno em exame.'''.format(M))
    E = float(input())
    NT = (M + E) / 2
    if NT >= 5:
        print('''Nota do exame: {}
Aluno aprovado.
Media final: {:.1f}'''.format(E, NT))
    else:
        print('''Nota do exame: {}
Aluno reprovado.
Media final: {}'''.format(E, NT))
