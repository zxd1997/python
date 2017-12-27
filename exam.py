a=int(input())
for i in range(a):
    b=0
    print("Class %d input number of student"%(i+1))
    b=int(input())
    print("Class %d input marks of student"%(i+1))
    for j in range(b):
        s = 0
        print("input marks of student ",j+1)
        for k in range(5):
            s+=int(input())
        print("total mark",s)
        print("averga",s/5)
