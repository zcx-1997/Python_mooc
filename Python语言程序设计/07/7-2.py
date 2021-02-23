# 文件字符分布
"""
    Time    : 2021/2/23 16:41
    Author  : 春晓
    FileName: 7-2.py
    Software: PyCharm
    Email   : zcx_demail@163.com
"""
f = open('latex.log')
count = 0
digits = {}
for i in range(26):
    digits[chr(ord('a')+i)] = 0

for line in f:
    for ch in line:
        digits[ch] = digits.get(ch,0) + 1
        count += 1
f.close()
for i in range(26):
    print("{}:{}".format(chr(ord('a')+i),digits[chr(ord('a')+i)]),end=',')

print("\nall：{}".format(count))