# 绘制七段数码管
"""
    Time    : 2021/2/20 10:11
    Author  : 春晓
    FileName: sevendigitdraw_v1.py
    Software: PyCharm
    Email   : zcx_demail@163.com
"""

import turtle


# 绘制空段
def drawGap():
    turtle.penup()
    turtle.fd(5)


# 绘制单段数码管
def drawLine(draw):

    drawGap()
    if draw:
        turtle.pendown()

    else:
        turtle.penup()

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

# 根据传入的字符绘制数字
def drawData(data):
    for i in data:
        drawDigit(eval(i))

def main():
    turtle.setup(800,400)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawData('20210220')

    turtle.hideturtle()  # 隐藏turtle箭头
    turtle.done()

if __name__ == "__main__":
    main()