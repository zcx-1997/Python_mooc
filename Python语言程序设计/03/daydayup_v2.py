# 天天向上 千分之五或百分之一
"""
    Time    : 2021/2/17 19:21
    Author  : 春晓
    FileName: daydayup_v2.py
    Software: PyCharm
    Email   : zcx_demail@163.com
"""


def day_365(dayfactor):
    dayup = pow(1+dayfactor,365)
    daydown = pow(1-dayfactor,365)

    print("up:{:.2f}，down:{:.2f}".format(dayup,daydown))

print("每天变强千分之五")
day_365(0.005)

print("每天变强百分之一")
day_365(0.01)
