N = int(input())
h = N//3600 
m = (N - (h*3600)) //60
s = ((N - (h*3600)) - (m*60))
print('{}:{}:{}'.format(h,m,s))
