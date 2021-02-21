# 《三国演义》人物出场统计
"""
    Time    : 2021/2/21 11:11
    Author  : 春晓
    FileName: calThreeKingdoms_v1.py
    Software: PyCharm
    Email   : zcx_demail@163.com
"""
import jieba

txt = open('threekingdoms.txt','r',encoding='utf-8').read()
words = jieba.lcut(txt)
counts = {}

for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)

for i in range(15):
    word, count = items[i]
    print("{:<10}{:>5}".format(word,count))