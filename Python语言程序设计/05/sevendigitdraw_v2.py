# 绘制七段数码管表示当前系统时间
"""
    Time    : 2021/2/20 10:39
    Author  : 春晓
    FileName: sevendigitdraw_v2.py
    Software: PyCharm
    Email   : zcx_demail@163.com
"""

import turtle
import time


# 绘制空段
def drawGap():
    turtle.penup()
    turtle.fd(5)


# 绘制单段数码管
def drawLine(draw):
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)


# 绘制七段数码管
def drawDigit(digit):
    drawLine(True) if digit in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 6, 8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)
    turtle.left(180)

    # 为下一个数字作准备
    turtle.penup()
    turtle.fd(20)


# 根据日期绘制, '%Y-%m=%d+'
def drawData(data):
    turtle.pencolor('red')
    for i in data:
        if i == '-':
            turtle.write('年', font=("Arial", 18, "normal"))
            turtle.pencolor('green')
            turtle.fd(40)
        elif i == '=':
            turtle.write('月', font=("Arial", 18, "normal"))
            turtle.pencolor('blue')
            turtle.fd(40)
        elif i == '+':
            turtle.write('日', font=("Arial", 18, "normal"))
        else:
            drawDigit(eval(i))


def main():
    turtle.setup(800, 400)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawData(time.strftime("%Y-%m=%d+", time.gmtime()))
    #    drawData('20210220')

    turtle.hideturtle()  # 隐藏turtle箭头
    turtle.done()


if __name__ == "__main__":
    main()
