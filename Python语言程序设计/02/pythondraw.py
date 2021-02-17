# 蟒蛇绘制
"""
    Time    : 2021/2/17 10:14
    Author  : 春晓
    FileName: pythondraw.py
    Software: PyCharm
    Email   : zcx_demail@163.com
"""

import turtle

turtle.setup(650,350,200,200)  #设置画布

turtle.penup()  #抬笔
turtle.fd(-250)  #前进-250（后退250）
turtle.pendown()  #落笔
turtle.pensize(25)  #画笔大小
turtle.pencolor('purple')  #画笔颜色
turtle.seth(-40)  #设置方向，默认正向右 ->, 角度逆时针

# 循环，绘制蟒蛇身体
for i in range(4):
    turtle.circle(40,80)  #绘制曲线（半径，角度）， 圆心在左侧
    turtle.circle(-40,80)

# 绘制蟒蛇脖子
turtle.circle(40,80/2)
turtle.fd(40)

# 绘制蟒蛇头部
turtle.circle(16,180)
turtle.fd(40 * 2/3)

turtle.done()  #绘制完毕后不自动退出
