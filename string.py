a=input()
n=len(a)-1
i=0
a=a.upper()
while n>i:
    if (a[i]!=a[n]):
        print("no")
        exit(0)
    n-=1
    i+=1
print("yes")