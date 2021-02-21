# 《沉默的羔羊》之最多单词
"""
    Time    : 2021/2/21 14:24
    Author  : 春晓
    FileName: 6-3.py
    Software: PyCharm
    Email   : zcx_demail@163.com
"""
import jieba

txt = open('沉默的羔羊.txt','r',encoding='utf-8').read()
words = jieba.lcut(txt)
counts = {}

for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word,0)+1

items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
print(items[0][0])

for i in range(10):
    k,c = items[i]
    print(k,c)