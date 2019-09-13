N = int(input())
a = N//365
m = (N - (a*365)) // 30
d = (N - (a*365)) - (m * 30)
print('''{} ano(s)
{} mes(es)
{} dia(s)'''.format(a,m,d))
