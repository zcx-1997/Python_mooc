# 自动轨迹绘制
"""
    Time    : 2021/2/23 9:49
    Author  : 春晓
    FileName: autodraw.py
    Software: PyCharm
    Email   : zcx_demail@163.com
"""
import turtle as t
# t.tilte("自动轨迹绘制")
t.setup(800,600,0,0)
t.pensize(5)
t.pencolor('red')

datals = []
f = open('data.txt')
print(f)
for line in f:
    line = line.replace('\n','')
    datals.append(list(map(eval, line.split(","))))
f.close()
print(datals)

for i in range(len(datals)):
    t.pencolor(datals[i][3],datals[i][4],datals[i][5])
    t.fd(datals[i][0])
    if datals[i][1]:
        t.right(datals[i][2])
    else:
        t.left(datals[i][2])

t.done()