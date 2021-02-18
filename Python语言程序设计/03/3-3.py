# 恺撒密码加密
"""
    Time    : 2021/2/18 9:40
    Author  : 春晓
    FileName: 3-3.py
    Software: PyCharm
    Email   : zcx_demail@163.com
"""
str = input("请输入明文：")

for i in range(len(str)):
    if str[i] == ' ':
        print(' ',end='')
    elif str[i] in ['x','y','z','X','Y','Z']:
        print(chr(ord(str[i])-23),end='')
    else:
        print(chr(ord(str[i])+3),end='')

