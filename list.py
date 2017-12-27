a=[[0 for i in range(3)]for j in range(3)]
for i in range(3):
    for j in range(3):
        a[i][j]=int(input())
for i in range(3):
    for j in range(3):
        print(a[i][j],end='')
    print()