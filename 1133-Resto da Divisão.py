X = int(input())
Y = int(input())
if X <Y:
    for i in range (X, Y):
        if i%5 == 2 or i%5 ==3:
            print(i)
elif X>Y:
    for i in range (Y, X):
        if i%5 == 2 or i%5 ==3:
            print(i)
