s = float(input())
if s<=400:
    print('''Novo salario: {:.2f}
Reajuste ganho: {:.2f}
Em percentual: 15 %'''.format(s*1.15, s*0.15))
elif s>400 and s<=800:
    print('''Novo salario: {:.2f}
Reajuste ganho: {:.2f}
Em percentual: 12 %'''.format(s*1.12, s*0.12))
elif s>800 and s<=1200:
    print('''Novo salario: {:.2f}
Reajuste ganho: {:.2f}
Em percentual: 10 %'''.format(s*1.10, s*0.10))
elif s>1200 and s<=2000:
    print('''Novo salario: {:.2f}
Reajuste ganho: {:.2f}
Em percentual: 7 %'''.format(s*1.07 , s*0.07))
elif s>2000:
    print('''Novo salario: {:.2f}
Reajuste ganho: {:.2f}
Em percentual: 4 %'''.format(s*1.04 , s*0.04))
