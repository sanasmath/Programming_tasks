print("starting from")
n=int(input())
print("end in")
m=int(input())

for x in range(n,m+1):
    if x%2==0:
        print(x,'even')
    else:
        print(x,'odd')
