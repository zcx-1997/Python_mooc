# 科赫曲线
"""
    Time    : 2021/2/20 11:20
    Author  : 春晓
    FileName: kochdraw_v1.py
    Software: PyCharm
    Email   : zcx_demail@163.com
"""
import turtle

def koch(size,n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            koch(size/3,n-1)

def main():
    turtle.setup(800,400)
    turtle.penup()
    turtle.goto(-300,-50)
    turtle.pendown()
    turtle.pensize(2)
    koch(600,3)
    turtle.hideturtle()

if __name__ == "__main__":
    main()