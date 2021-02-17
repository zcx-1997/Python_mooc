# 绘制风轮
"""
    Time    : 2021/2/17 14:07
    Author  : 春晓
    FileName: 2-4.py
    Software: PyCharm
    Email   : zcx_demail@163.com
"""

import turtle

turtle.pensize(5)

for i in range(4):
    turtle.left(45)
    turtle.fd(150)
    turtle.left(90)
    turtle.circle(150,45)
    turtle.left(90)
    turtle.fd(150)
turtle.done()