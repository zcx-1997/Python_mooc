# turtle库的简单使用1
"""
    Time    : 2021/2/17 10:48
    Author  : 春晓
    FileName: turtle_learn1.py
    Software: PyCharm
    Email   : zcx_demail@163.com
"""

import turtle

# turtle的绘图窗体（画布）
# turtle.setup(width,height,startx,starty)
turtle.setup(800,400)  #默认屏幕中心
turtle.setup(800,400,0,0)  #屏幕左上角


# turtle空间坐标体系，turtle默认在坐标原点（0,0），朝向正右
# turtle.goto(x,y)  # 爬向目标坐标(x,y)
turtle.goto(100,100)
turtle.goto(-100,100)
turtle.goto(-100,-100)
turtle.goto(100,-100)
turtle.goto(0,0)

# turtle.fd(lengh) 前进,turtle.bk(leng) 后退,turtle.circle(r,angle)曲线

# turtle角度坐标体系，turtle默认在画布中心（0,0），朝向正右,角度按逆时针递增
# turtle.seth(angle)  只改变方向，angle为绝对角度数
# turtle.left(angle),turtle.right(angle)  angle为相对角度

turtle.fd(100)
turtle.seth(45)
turtle.fd(150)
turtle.right(135)
turtle.fd(300)
turtle.left(135)
turtle.fd(150)

# RGBs色彩模式
# turtle.colormode(mode) mode: 1.0:小数模式(默认)；255:整数值模式,
turtle.color('blue')
turtle.left(90)
turtle.fd(50)

turtle.color(0,0,1)
turtle.right(90)
turtle.fd(50)

turtle.colormode(255)
turtle.left(90)
turtle.fd(50)
turtle.done()