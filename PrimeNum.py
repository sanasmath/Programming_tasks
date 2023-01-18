print('you can find primery numbers here. please enter the starting range')
n=int(input())
print('ending ranage')
m=int(input())

for x in range (n,m+1):
    if x > 1:
        for p in range (2,x):
            if x%p ==0:
                break
        else:
             print(x)