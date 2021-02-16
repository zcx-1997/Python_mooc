# 温度转换
"""
    Time    : 2021/2/15 20:43
    Author  : 春晓
    FileName: temp_convert.py
    Software: PyCharm
    Email   : zcx_demail@163.com
"""

temp_str = input('请输入带有符号的温度值：')

if temp_str[-1] in ['f','F']:
    c = (eval(temp_str[:-1])-32) / 1.8
    print('转换后的温度值是{:.2f}C'.format(c))
elif temp_str[-1] in ['c','C']:
    f = eval(temp_str[:-1]) * 1.8 + 32
    print('转换后的温度是：{:.2f}F'.format(f))
else:
    print('输入格式错误')