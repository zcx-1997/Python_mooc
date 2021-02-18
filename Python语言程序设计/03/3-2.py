# 星号三角形
"""
    Time    : 2021/2/18 9:18
    Author  : 春晓
    FileName: 3-2.py
    Software: PyCharm
    Email   : zcx_demail@163.com
"""
N = eval(input("请输入一个奇数："))
if N % 2 != 0:
    for i in range(N):
        if i % 2 == 0:
            s = '*' * (i+1)
            print(s.center(N,' '))
else:
    print("输入格式错误，请重新输入！")