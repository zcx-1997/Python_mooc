# 文件独特行数
"""
    Time    : 2021/2/23 17:03
    Author  : 春晓
    FileName: 7-3.py
    Software: PyCharm
    Email   : zcx_demail@163.com
"""
f = open('latex.log')
all_lines = f.readlines()
f.close()

line_1 = set(all_lines)
for line in line_1:
    all_lines.remove(line)
line_2 = set(all_lines)

print("共 {} 独特行。".format(len(line_1)-len(line_2)))