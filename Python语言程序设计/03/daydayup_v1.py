# 天天向上 千分之一
"""
    Time    : 2021/2/17 19:17
    Author  : 春晓
    FileName: daydayup_v1.py
    Software: PyCharm
    Email   : zcx_demail@163.com
"""

day_up = pow(1.001,365)
day_down = pow(0.999,365)

print("向上：{:.2f}，向下：{:.2f}".format(day_up,day_down))