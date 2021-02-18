# 天天向上，需要努力的程度
"""
    Time    : 2021/2/17 19:50
    Author  : 春晓
    FileName: daydayup_v4.py
    Software: PyCharm
    Email   : zcx_demail@163.com
"""

def day_up(df):
    dayup=1
    for i in range(365):
        if i % 7 in [0,6]:
            dayup = dayup*(1-0.01)
        else:
            dayup = dayup*(1+df)
    return dayup

dayfactor = 0.01
while day_up(dayfactor) < 37.78:
    dayfactor += 0.001

print("工作日的努力程度是：{:.3f}".format(dayfactor))