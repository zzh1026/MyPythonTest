# -*- coding: utf-8 -*-

# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖

height = 1.75
weight = 80.5
list = ('过轻', '正常', '过重', '肥胖', '严重肥胖')

bmi = weight / (height * height)

index = 0;
if bmi < 18.5:
    index = 0
elif bmi < 25:
    index = 1
elif bmi < 28:
    index = 2
elif bmi < 32:
    index = 3
else:
    index = 4

print('小明的身高为:{0}cm,体重为:{1}kg,其BMI = {2:.4f},其体重 -{3}'.format(height, weight, bmi, list[index]))
