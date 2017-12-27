print("Hello World")
a = 3
b = 20
print("b is", b, a, a**b)
if (0<=a<=100):
    print("yes")
if (a > b and a>0):
    print(a+9)
    print("a喵喵喵")
    print("None")
    if (0<b<a):
        a*=5
        print(a)
        print("这是if嵌套if的格式，缩进统一的就是同一层")
else:
    print(b)
print("这是if外面的东西，无论如何都会执行")
print(b>10)
print(max(a,b))