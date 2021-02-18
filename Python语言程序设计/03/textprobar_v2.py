# 单行刷新文本进度条
"""
    Time    : 2021/2/18 8:56
    Author  : 春晓
    FileName: textprobar_v2.py
    Software: PyCharm
    Email   : zcx_demail@163.com
"""
import time

scale = 10
print("{:=^25}".format('START'))

for i in range(scale+1):
    a = '=' * i
    b = '.' * (scale-i)
    c = (i/scale) * 100
    print("\r{:3.0f}%[{}>{}]".format(c,a,b),end='')
    time.sleep(0.3)
print('\n{:=^23}'.format('END'))
