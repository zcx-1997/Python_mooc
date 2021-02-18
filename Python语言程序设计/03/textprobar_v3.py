# 文本进度条 完整效果
"""
    Time    : 2021/2/18 9:02
    Author  : 春晓
    FileName: textprobar_v3.py
    Software: PyCharm
    Email   : zcx_demail@163.com
"""

import time

scale = 20
print('START'.center(scale,'='))
start = time.perf_counter()

for i in range(scale+1):
    a = '=' * i
    b = '.' * (scale-i)
    c = (i/scale) * 100
    dur = time.perf_counter() - start
    print("\r{:3.0f}%[{}>{}] {:.2f}s".format(c,a,b,dur),end='')
    time.sleep(0.2)

print('\n'+"END".center(scale,'='))
