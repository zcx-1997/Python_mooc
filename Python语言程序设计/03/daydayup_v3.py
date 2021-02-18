# 天天向上，工作日的力量
"""
    Time    : 2021/2/17 19:46
    Author  : 春晓
    FileName: daydayup_v3.py
    Software: PyCharm
    Email   : zcx_demail@163.com
"""

dayup = 1.0
dayfactor = 0.01

for i in range(365):
    if i % 7 in [0,6]:
        dayup = dayup*(1-dayfactor)
    else:
        dayup = dayup*(1+dayfactor)

print("工作日的力量：{:.2f}".format(dayup))