x = input().split (' ')
di = int(x[1])
n = input().split(' : ')
hi = int(n[0])
mi = int(n[1])
si = int(n[2])
x = input().split(' ')
df = int(x[1])
n = input().split(' : ')
hf = int(n[0])
mf = int(n[1])
sf = int(n[2])
I = (hi * 3600 + mi * 60 + si) - 86400
F =  hf * 3600 + mf * 60 + sf
T = I+F 
h = T%86400
if di==df:
    print('0 dia(s)')
else:
    if T >= 86400:
        print('{} dia(s)'.format( (T//86400) + (df-di-1) ))
        if T%86400 >= 3600:
            print('{} hora(s)'.format( h//3600 ))
            if h%3600 >= 60:
                print('{} minuto(s)'.format( h%3600//60 ))
                print('{} segundo(s)'.format( ((h%3600) % 60 ))
            if h%3600 < 60:
                print('')
                
    else:
        print()


"""    
    print(df-di-1,'dia(s)')

if I>=F:
    print('''{} hora(s)
{} minuto(s)
{} segundo(s)
'''
.format(I//3600,
        (I%3600)//60,
        (I%3600)%60))
if I>=F:
    print('''{} hora(s)
{} minuto(s)
{} segundo(s)
'''
.format(I//3600,
        (I%3600)//60,
        (I%3600)%60))
    


'''

if hi > hf:
    print(23 - hi +hf,'hora(s)')
else:
    print(hf-hi,'hora(s)')
if mi > mf :
    print(59 - mi + mf,'minuto(s)')
else:
    print(mf - mi,'minuto(s)')
if si > sf :
    print(59-si + sf,'segundo(s)')
else:
    print(sf -si,'segundo(s)')


        

df-di,

hi > hf
24 - hi + hf,

hf > hi
hf-hi

mi > mf
60 -mi + mf

mf > mi
mf - mi

si > sf
60 - si + sf

sf > si
sf - si





print(hi, mi, si)

print(hf,mf ,sf)
'''

"""
