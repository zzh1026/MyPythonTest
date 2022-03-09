#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Created by zhaozehui at 2019/11/29
# 靳玉丽的统计数据,根据步长统计区段内个数
__author__ = 'zzh'

import pandas as pd  # 数据处理

# 元数据位置 , 需要设置
datas = pd.read_excel('/Users/didi/Documents/num_to_zzh.xlsx')

# 要分割的步长, 需要设置 ,此处单位为M
dM = 1000000
dT = dM

# 输出的位置,需要设置
resultPath = '/Users/didi/Documents/num_to_zzh_result_%sM.xlsx' % (dT // dM)

# 打印头,看数据是否准确
# print(datas.head())
# 打印分段描述信息
# print(datas.describe())

# 分割起始位置
start = 0
# 区间的列表
qujian = [start]
# 区间的列表对应的标签
qujian_lable = []

# 拿到 position 列的数据
datas = datas['Start']
# heads = datas.head()
# print(str(heads))

# 循环,以0开始,间隔为步长拿到分段列表
while True:
    end = start + dT
    # 标签添加数据内容为 [0M-1M, 1M-2M ...]等等用来进行自己查看,这个可以不使用
    qujian_lable.append('%sM- %sM' % (start / dM, end / dM))
    # 完善区间,用来最后对数据进行分割统计,内容为 [0,dT, 2*dT,3*dT...]
    qujian.append(end)
    start = end
    if start > datas.max():
        break

# 切割数据
result_cut = pd.cut(datas, bins=qujian, right=False, labels=qujian_lable, include_lowest=True, retbins=False)
# print(qujian)
# print(qujian_lable)
print(result_cut.head())
# lists = list(result_cut)
# result_data = pd.Series(lists)
# print(result_data)
# print('数据数量为: %s' % (lists.__len__()))
# print('数据数量为: %s' % (datas.count()))

results = result_cut.value_counts(sort=False, ascending=True)
print(results)

# 写出到xlsx文件
# results.to_excel(resultPath)


