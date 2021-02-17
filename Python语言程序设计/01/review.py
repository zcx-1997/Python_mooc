# 复习：温度转换实例
"""
    Time    : 2021/2/17 9:02
    Author  : 春晓
    FileName: review.py
    Software: PyCharm
    Email   : zcx_demail@163.com
"""

temp = input("请输入带有符号的温度值：")

if temp[-1] in ['F','f']:
    c = (eval(temp[:-1]) - 32) / 1.8
    print("转换后的温度值为：{:.2f}C.".format(c))
elif temp[-1] in ['C','c']:
    f = eval(temp[:-1]) * 1.8 + 32
    print("转换后的温度值为：{:.2f}F.".format(f))