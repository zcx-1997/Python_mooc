# 任意累积
"""
    Time    : 2021/2/20 11:30
    Author  : 春晓
    FileName: 5-1.py
    Software: PyCharm
    Email   : zcx_demail@163.com
"""


def cmul(*n):
    num = 0
    # print(n)
    for i in n:
        # print(i)
        num += i
    return num

print(eval("cmul({})".format(input())))
