# 政府工作报告词云
"""
    Time    : 2021/2/23 16:18
    Author  : 春晓
    FileName: govrptWC.py
    Software: PyCharm
    Email   : zcx_demail@163.com
"""
import jieba
import wordcloud

f = open("新时代中国特色社会主义.txt",'r',encoding='utf-8')
t = f.read()
f.close()
txt = ' '.join(jieba.lcut(t))
w = wordcloud.WordCloud(font_path="msyh.ttc",background_color='white',\
                        width=1000,height=700)
w.generate(txt)
w.to_file("grwordcloud.png")