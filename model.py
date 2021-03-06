import random  # 导入random类
class file:  # 论文类
    def __init__(self, id):  # 构造方法，传入id
        self.id = id  # 赋值给id
        self.count = 5  # 论文需要改的次数为6（5次+最后一次改完被剔除）
files = []  # 存论文的list
works = {}  # 存老师和老师的任务的字典
n = int(input())  # 读取论文数量
for i in range(n):
    files.append(file(input()))  # 存入list，使用file类的构造函数实例化一个file类，并且赋予id的值
m = int(input())  # 读取老师数量
for i in range(m):
    works[input()] = []  # 老师信息作为字典的key，创建一个空list作为字典的key对应值，用于存放老师的任务
while n != 0:  # 当论文没被拿完。进行循环分配
    for s in works:  # 遍历所有老师（这样是取出字典的key，也就是老师信息）s则是当前哪个老师在取论文
        if n == 0: break  # 如果论文已经被取完了就break，不然随机数和访问list会出错
        x = random.randint(0, n - 1)  # 再0到当前剩下的论文份数间生成随机数
        i = 0
        while files[x].id[0:5] == s[0:5] and i < n:  # 若是当前取论文的老师的专业编号和随机取到的论文相同则放回
            x = random.randint(0, n - 1)  # 重新生成随机数
            i += 1  # i是用于一种情况，生成了n个随机数，还是没有可以用的，但是还有论文，说明剩下都是这个专业的论文了，不break就陷入死循环
        if files[x].id[0:5] != s[0:5]:  # 再次判断是不是本专业的（因为有可能是都剩下本专业的而强行break出来的
            if files[x].count == 0:  # 论文还需要被改的次数为0
                n -= 1  # 论文剩下的份数-1
                works[s].append(files[x].id)  # 论文存入老师的任务列表
                files.remove(files[x])  # 从论文列表内删除该论文
            else:
                files[x].count -= 1  # 论文需要再被改的次数-1
                works[s].append(files[x].id)  # 论文存入老师的任务列表
for i in works:  # 遍历所有老师，输出
    print(i, works[i])  # i是key，就是老师信息，works[i]用key访问字典对应的项目，是个list，输出
