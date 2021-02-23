# 文件行数
"""
    Time    : 2021/2/23 16:33
    Author  : 春晓
    FileName: 7-1.py
    Software: PyCharm
    Email   : zcx_demail@163.com
"""
f = open('latex.log')
n = 0
for line in f:
    if len(line) != 0:
        n += 1
print(n)
f.close()