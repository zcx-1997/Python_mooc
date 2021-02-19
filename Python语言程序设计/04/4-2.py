# 三位水仙花数
"""
    Time    : 2021/2/19 12:05
    Author  : 春晓
    FileName: 4-2.py
    Software: PyCharm
    Email   : zcx_demail@163.com
"""
for i in range(1,10):
    n1=i**3
    for j in range(10):
        n2 = j ** 3
        for z in range(10):
            n3 = z ** 3
            num = i*100+j*10+z
            if n1+n2+n3 == num:
                print(num,end=',')
