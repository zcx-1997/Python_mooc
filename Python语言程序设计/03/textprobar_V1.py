# 文本进度条
"""
    Time    : 2021/2/18 8:31
    Author  : 春晓
    FileName: textprobar_V1.py
    Software: PyCharm
    Email   : zcx_demail@163.com
"""

import time

scale = 10
print('START'.center(25,'='))

for i in range(scale+1):
    a = '=' * i
    b = '.' * (scale-i)
    c = (i/scale) * 100
    print("{:^3.0f}%[{}>{}]".format(c,a,b))
    time.sleep(0.3)
print('END'.center(23,'='))