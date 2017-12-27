def chk(x):
    i=2
    f=True
    while i<(x/2):
        if x%i==0:
            f=False
            break
        i+=1
    return f
i=2
while i<100:
    if chk(i):print(i,end=" ")
    i+=1