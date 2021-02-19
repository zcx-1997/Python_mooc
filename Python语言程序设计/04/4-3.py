# 用户登录的三次机会
"""
    Time    : 2021/2/19 12:13
    Author  : 春晓
    FileName: 4-3.py
    Software: PyCharm
    Email   : zcx_demail@163.com
"""

name = 'Kate'
pwd = 666666


for i in range(3):
    input1 = input("请输入用户名：")
    input2 = eval(input("密码："))
    if input1 == name and input2 == pwd:
        print("登录成功！")
        break
    elif i == 2:
        print("3次用户名或者密均有误！退出程序")
