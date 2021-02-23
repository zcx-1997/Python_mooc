# csv数据格式清洗
"""
    Time    : 2021/2/23 17:26
    Author  : 春晓
    FileName: 7-5.py
    Software: PyCharm
    Email   : zcx_demail@163.com
"""
fi = open('data.csv')
for line in fi:
    line = line.replace('\n','')
    line = line.split(',')
    for w in line:
        w = w.strip()
        print(w,end=',')
    print('\n')
fi.close()
