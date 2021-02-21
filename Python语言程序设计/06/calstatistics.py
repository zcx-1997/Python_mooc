# 基本统计值计算
"""
    Time    : 2021/2/21 9:33
    Author  : 春晓
    FileName: calstatistics.py
    Software: PyCharm
    Email   : zcx_demail@163.com
"""

def getNum():
    nums = []

    iNum = input("请输入数字（回车退出）：")
    while iNum != "":
        nums.append(eval(iNum))
        iNum = input("请输入数字（回车退出）：")
    return nums


def mean(numbers):
    s = 0.0
    for num in numbers:
        s += num
    return s / len(numbers)


def dev(numbers,mean):
    sdev = 0.0
    print(numbers)
    for num in numbers:
        sdev += (num-mean)**2
        print(sdev)
    return pow(sdev/(len(numbers)-1),0.5)

def media(numbers):
    sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (numbers[size//2-1] + numbers[size//2]) / 2
    else:
        med = numbers[size//2]
    return med

n = getNum()
m = mean(n)

print("平均值：{}，标准差：{}，中位数：{}".format(m,dev(n,m),media(n)))