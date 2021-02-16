# 五角星绘制
"""
    Time    : 2021/2/16 8:56
    Author  : 春晓
    FileName: 1-3.py
    Software: PyCharm
    Email   : zcx_demail@163.com
"""

import turtle

turtle.color('red','red')  #线color，填充color
turtle.begin_fill()
for i in range(5):
    turtle.fd(200)
    turtle.rt(144)
turtle.end_fill()
turtle.done()  #绘制完毕后不自动退出