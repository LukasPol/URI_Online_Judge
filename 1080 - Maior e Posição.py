n=[]
for i in range(100):
    n.append(int(input()))

x = max(n)
print(x)
print(n.index(x)+1)

