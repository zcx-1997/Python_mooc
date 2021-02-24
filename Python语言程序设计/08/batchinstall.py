# 第三方库自动安装脚本
"""
    Time    : 2021/2/24 9:38
    Author  : 春晓
    FileName: batchinstall.py
    Software: PyCharm
    Email   : zcx_demail@163.com
"""
import os

libs = ['numpy','matplotlib','pillow','sklearn','requests','django','pyqt5','pandas']

try:
    for lib in libs:
        os.system("pip install "+lib)
    print("Successful")
except:
    print("Failed Somehow")