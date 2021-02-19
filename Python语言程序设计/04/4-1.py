# 加减和
"""
    Time    : 2021/2/19 12:00
    Author  : 春晓
    FileName: 4-1.py
    Software: PyCharm
    Email   : zcx_demail@163.com
"""

sum  = 0
for i in range(1,967):
    if i % 2 != 0:
        sum += i
    else:
        sum -= i

print("sum:{}".format(sum))
