# time库的简单使用
"""
    Time    : 2021/2/17 19:59
    Author  : 春晓
    FileName: time_learn.py
    Software: PyCharm
    Email   : zcx_demail@163.com
"""

import time

# 获取时间并格式化
print(time.ctime())
print(time.gmtime())
print(time.localtime())
# now = time.gmtime()
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

# 程序计时
# time.perf_counter()  返回一个CPU级别的精确时间计数值，单位为妙

start = time.perf_counter()
# time.sleep(3)
end = time.perf_counter()
print(end-start)