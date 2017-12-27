c=0
s=0
while c<5:
    try:
        num=int(input())
        c+=1
        s+=num
    except:
        print("error")
print(s)