# 斐波那契数列
"""
    Time    : 2021/2/20 11:39
    Author  : 春晓
    FileName: 5-2.py
    Software: PyCharm
    Email   : zcx_demail@163.com
"""
def fbi(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fbi(n-1) + fbi(n-2)


n = eval(input())
print(fbi(n))
