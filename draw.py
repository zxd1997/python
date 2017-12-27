a=int(input())
i=0
while (i<a):
    j=0
    k=0
    while (k<(a-i)):
        print("  ",end='')
        k+=1
    while (j<=i):
        print(" * ",end=' ')
        j+=1
    print()
    i+=1
# i=a-1
# while (i>=0):
#     j=0
#     k=0
#     while (k<=(a-i)):
#         print("  ",end='')
#         k+=1
#     while (j<i):
#         print(" * ",end=' ')
#         j+=1
#     print()
#     i-=1
