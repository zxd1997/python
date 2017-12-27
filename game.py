import random
s=0
t=0
while True:
    a=random.randint(0, 99)
    print(a)
    t+=1
    i=0
    f=False
    while (i<3):
        b = int(input())
        if (b>a):
            print("TOO BIG")
        elif (b<a):
            print("TOO LESS")
        elif (b==a):
            print("RIGHT")
            s+=1
            break
        i+=1
    print("continue? Y/N")
    c=input()
    if c=='N':break
print('generate %d randomint, total %d right'%(t,s))