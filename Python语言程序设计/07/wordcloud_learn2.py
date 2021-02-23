# wordcloud库的使用
"""
    Time    : 2021/2/23 16:12
    Author  : 春晓
    FileName: wordcloud_learn2.py
    Software: PyCharm
    Email   : zcx_demail@163.com
"""

import jieba
import wordcloud
txt = "程序设计语言是计算机能够理解和识别用户操作意图的一种交互体系，它按照特定规则组织计算机指令，使计算机能够自动进行各种运算处理。"

w = wordcloud.WordCloud(width=1000,height=700,font_path="msyh.ttc")
w.generate(' '.join(jieba.lcut(txt)))
w.to_file("pywcloud2.png")