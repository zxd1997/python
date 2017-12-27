a=input()
b=input()
c=[]
d=[]
for i in range(len(a)):
    c.append(a[i])
for i in range(len(b)):
    c.append(b[i])
for i in range(len(c)):
    print(c[i],end='')
print()
if len(a)!=len(b):
    print("no")
else:
    f=True
    for i in range(len(a)):
        if (a[i]!=b[i]):
            f=False
            print("no")
            if a[i]>b[i]:print('a>b')
            else:print("b>a")
            break
    if f:print("yes")
for i in range(len(c)):
    d.append(c[i])
for i in range(len(c)):
    print(d[i],end='')
print()
