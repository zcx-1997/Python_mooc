# 《三国演义》人物出场统计
"""
    Time    : 2021/2/21 11:19
    Author  : 春晓
    FileName: calThreeKingdoms_v2.py
    Software: PyCharm
    Email   : zcx_demail@163.com
"""

import jieba

import jieba
txt = open('threekingdoms.txt','r',encoding='utf-8').read()
excludes = {"将军","却说","荆州","二人","不可","不能","如此","商议","如何","主公","军士","左右","军马","引兵","次日","大喜","天下","东吴","于是","今日"}
words = jieba.lcut(txt)
counts = {}

for word in words:
    if len(word) == 1:
        continue
    elif word == "诸葛亮" or word == "孔明曰":
        rword = "孔明"
    elif word == "关公" or word == "云长":
        rword = "关羽"
    elif word == "玄德" or word == "玄德曰":
        rword = "刘备"
    elif word== "孟德" or word == "丞相":
        rword = "曹操"
    else:
        rword = word
    counts[rword] = counts.get(rword,0) + 1

for word in excludes:
    del counts[word]

items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)

for i in range(5):
    word, count = items[i]
    print("{:<10}{:>5}".format(word,count))
