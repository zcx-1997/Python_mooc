# 计算国际国内身体质量指标 BMI
"""
    Time    : 2021/2/19 11:08
    Author  : 春晓
    FileName: calBMI.py
    Software: PyCharm
    Email   : zcx_demail@163.com
"""

height, weight = eval(input("请输入身高（米）和体重（公斤）[逗号隔开]："))
bmi = weight / pow(height,2)
print("BMI的值为：{:.2f}".format(bmi))

grade_w,grade_c = '',''
if bmi < 18.5:
    grade_w,grade_c = "偏瘦","偏瘦"
elif bmi < 24:
    grade_w, grade_c = "正常", "正常"
elif bmi < 25:
    grade_w, grade_c = "正常", "偏胖"
elif bmi < 28:
    grade_w, grade_c = "偏胖", "偏胖"
elif bmi < 30:
    grade_w, grade_c = "偏胖", "肥胖"
else:
    grade_w, grade_c = "肥胖", "肥胖"

print("BMI指标在国际：{}，国内：{}".format(grade_w,grade_c))