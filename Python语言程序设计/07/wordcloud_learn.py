# wordcloud 库的使用
"""
    Time    : 2021/2/23 16:09
    Author  : 春晓
    FileName: wordcloud_learn.py
    Software: PyCharm
    Email   : zcx_demail@163.com
"""
import wordcloud
txt = "life is short,you need python"

w = wordcloud.WordCloud(background_color='white')
w.generate(txt)
w.to_file("pywcloud.png")
