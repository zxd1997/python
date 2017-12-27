while True:
    a=input()
    if len(a)!=8:
        print("wrong")
        continue
    b=int(a[0:4])
    c=int(a[4:6])
    d=int(a[6:8])
    if (0>c or c>12):
        print("wrong1")
        continue
    if (d>31 or d<0):
        print("wrong2")
        continue
    if (c==2 and (d!=28 or  d!=29)):
        print("wrong3")
        continue
    break
e=[0,31,28,31,30,31,30,31,31,30,31,30,31]
print(b," ",c," ",d)
sum=d
for i in range(0,c):
    sum+=e[i]
if (c>2)and(b%400==0 or (b%400!=0 and b%4==0)):sum+=1
print(sum)