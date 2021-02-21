#　hamlet英文词频统计
"""
    Time    : 2021/2/21 10:56
    Author  : 春晓
    FileName: calhamlet.py
    Software: PyCharm
    Email   : zcx_demail@163.com
"""
def getText():
    txt = open('hamlet.txt','r').read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\]^_‘{|}~':
        txt = txt.replace(ch," ")
    return txt

hamlet = getText()
words = hamlet.split()
counts = {}

for word in words:
    counts[word] = counts.get(word,0)+1
items = list(counts.items())
print(items[0])
items.sort(key=lambda x:x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print("{:<10}{:>5}".format(word,count))

