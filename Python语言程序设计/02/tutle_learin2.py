# turtle库的简单使用2

"""
    Time    : 2021/2/17 13:23
    Author  : 春晓
    FileName: tutle_learin2.py
    Software: PyCharm
    Email   : zcx_demail@163.com
"""

import turtle

# turtle画笔控制函数
turtle.penup()
turtle.pendown()
turtle.pensize(5)
turtle.pencolor('purple')


# turtle运动控制函数
turtle.fd(100)

# turtle.circle(r,extent=None)
turtle.circle(50)
turtle.fd(100)
turtle.circle(50,180)


# turtle方向控制函数
# turtle.seth(angle)  改变行进方向，angle：绝对角度
# turtle.left(angle)  turtle.right(angle)   angle：当前行进方向上旋转的角度

turtle.done()