# random库的简单使用
"""
    Time    : 2021/2/19 11:27
    Author  : 春晓
    FileName: random_learn.py
    Software: PyCharm
    Email   : zcx_demail@163.com
"""

import random

# 设置随机数种子
random.seed(10)

# 生成一个 0~1之间的随机小数,因为设置了seed，所以第一个数必为 0.5714025946899135
print(random.random())
print(random.random())

# 生成一个在[10,100]之间的随机整数
print(random.randint(10,100))
# 生成一个在[10,100之间以5为步长的随机整数
print(random.randrange(10,100,5))

# 生成一个[10,100]之间的随机小数
print(random.uniform(10,100))

# 从序列中随机选取一个元素
print(random.choice([0,1,2,3,4,5,6,7,8,9]))

# 将序列中元素随机排列
s = [0,1,2,3,4,5,6,7,8,9]
random.shuffle(s)
print(s)

# print(random.shuffle([0,1,2,3,4,5,6,7,8,9])) error