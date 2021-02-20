# 汉诺塔
"""
    Time    : 2021/2/20 11:41
    Author  : 春晓
    FileName: 5-3.py
    Software: PyCharm
    Email   : zcx_demail@163.com
"""
steps = 0
def hanoi(src, des, mid, n):
    global steps
    if n == 1:
        steps += 1
        print("[STEP{:>4}] {}->{}".format(steps, src, des))
    else:

        hanoi(src,mid,des,n-1)
        steps += 1
        print("[STEP{:>4}] {}->{}".format(steps, src, des))
        hanoi(mid,des,src,n-1)

N = eval(input())
hanoi("A", "C", "B", N)