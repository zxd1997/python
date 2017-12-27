a=[[0 for i in range(5)]for j in range(10)]
n=int(input())
for i in range(n):
    for j in range(3):
        a[i][j]=int(input())
        a[i][4]+=a[i][j]
for i in range(n):
    for j in range(i,n):
        if a[i][4]<a[j][4]:
            t=a[i]
            a[i]=a[j]
            a[j]=t
for i in range(n):
    print(a[i][4])