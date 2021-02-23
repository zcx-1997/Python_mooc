# csv格式列变换
"""
    Time    : 2021/2/23 17:13
    Author  : 春晓
    FileName: 7-4.py
    Software: PyCharm
    Email   : zcx_demail@163.com
"""
fi = open('data.csv')
for line in fi:
    line = line.replace('\n','')
    line = line.split(',')
    line.reverse()
    for w in line:
        print(w,end=',')
    print('\n')
fi.close()