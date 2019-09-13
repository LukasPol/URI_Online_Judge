pa = 0
im = 0
po = 0
ne = 0
for i in range (5):
    n = int(input())
    if n %2 == 0 :
        pa+=1
    else:
        im+=1
    if n >0:
        po+=1
    elif n<0:
        ne+=1
print('''{} valor(es) par(es)
{} valor(es) impar(es)
{} valor(es) positivo(s)
{} valor(es) negativo(s)'''
      .format(pa,im,po,ne))
