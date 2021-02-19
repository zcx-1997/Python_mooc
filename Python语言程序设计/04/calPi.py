# 计算圆周率 pi（蒙特卡罗方法）
"""
    Time    : 2021/2/19 11:45
    Author  : 春晓
    FileName: calPi.py
    Software: PyCharm
    Email   : zcx_demail@163.com
"""

import random
import time

points = 1000 * 1000 * 10
area = 0
start = time.perf_counter()
for i in range(points):
    x,y = random.random(),random.random()
    dist = pow(x*x+y*y,0.5)

    if dist <= 1.0:
        area  += 1
pi = 4 * (area/points)
print("圆周率为：{}".format(pi))
print("计算时间为：{:.2f}s".format(time.perf_counter()-start))