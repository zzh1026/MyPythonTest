#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# create by zzh

#   迭代
#
# 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。

# 在Python中，迭代是通过for ... in来完成的

lists = [1, 2, 3, 4, 5, 6]  # list集合
for x in lists:
    # print(x)
    pass

tuples = (1, 2, 3, 4, 5, 6)  # tuple , 不可变list集合
for x in lists:
    # print(x)
    pass

# 因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。
dicts = {'a': 1, 'b': 2, 'c': 3, 'a': 1, 'b': 2, 'c': 3}  # dict 字典 , key-value
for key in dicts:
    # print('key=%s, value=%s' % (key, dicts[key]))
    pass

for value in dicts.values():  # 迭代value
    # print(value)
    pass

for item in dicts.items():  # 迭代item
    for x in item:
        # print(x)
        pass
    pass

# 由于字符串也是可迭代对象，因此，也可以作用于for循环：
str = 'lksddf'
for char in str:
    # print(char)
    pass

from collections import Iterable

# 判断一个数据是否可迭代
# print(isinstance('skldjf', Iterable))  # str是否可迭代
# print(isinstance([1, 2, 3], Iterable))  # list是否可迭代
# print(isinstance(123, Iterable))  # 整数是否可迭代

# print(isinstance(10, int))    # 整数是否是int类型

# 如果要对list实现类似Java那样的下标循环怎么办？
# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for i, value in enumerate(['A', 'B', 'C']):
    # print(i, value)
    pass

# for循环里，同时引用了两个变量，在Python里是很常见的，比如下面的代码：
for x, y in [(1, 1), (2, 4), (3, 9)]:  # 一个list集合, 每个元素是一个tuple
    # print(x, y)
    pass

for x in [(1, 1), (2, 4), (3, 9)]:  # 一个list集合, 每个元素是一个tuple
    # print(x)
    pass


# 测试:使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L=None):
    if L is None or len(L) == 0:
        return None, None
    min, max = L[0], L[0]
    for item in L:
        if min > item:
            min = item
        elif max < item:
            max = item
    return min, max


L = [2, 3, 5, 1, 8, 5]
# print(findMinAndMax(L))

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
