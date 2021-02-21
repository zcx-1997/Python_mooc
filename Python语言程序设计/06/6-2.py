# 字典翻转输出
"""
    Time    : 2021/2/21 14:05
    Author  : 春晓
    FileName: 6-2.py
    Software: PyCharm
    Email   : zcx_demail@163.com
"""
str_in = input("请输入字典类型的字符串：")
# print(str_in)
ori_dic = eval(str_in)
if isinstance(ori_dic,dict):
    # print(ori_dic)
    fin_dic = {}

    for k,v in ori_dic.items():
        fin_dic[v] = k
        # print(k,v)
    print(fin_dic)

else:
    print("输入格式错误")