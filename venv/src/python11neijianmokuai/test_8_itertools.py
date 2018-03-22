#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 注释 '

__author__ = 'zzh'

#
# itertools
#
# Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。
import itertools

# 1, count()会创建一个无限的迭代器(无限迭代)
natuals = itertools.count(1, 2)
# for n in natuals:
#     print(n)

# 2, cycle()会把传入的一个序列无限重复下去(无限迭代)
cs = itertools.cycle('sdkfj')
# for c in cs:
#     print(c)

# 3, repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数(无限迭代)
re = itertools.repeat('A', 10)
# for i in re:
#     print(i)

#
# 无限序列只有在for迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，它不会事先把无限个元素生成出来，事实上也不可能在内存中创建无限多个元素。
# 无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
li = list(ns)
# print(li)

# 4, chain()可以把一组迭代对象串联起来，形成一个更大的迭代器(不无限,数量为迭代对象组的总和)
its = itertools.chain('abc', 'xyz')
# for i in its:
#     print(i)

# 5, groupby()把迭代器中相邻的重复元素挑出来放在一起
its = itertools.groupby('aaaabbbdddccccccl')
for i, v in its:
    # print(list(v))
    pass


# 练习
#
# 计算圆周率可以根据公式
# 利用Python提供的itertools模块，我们来计算这个序列的前N项和
def pi(N):
    # ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    natures = itertools.count(1, 2)

    natures = [2 * x - 1 for x in range(1, N + 1)]

    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    ns = itertools.takewhile(lambda x: x <= 2 * N - 1, natures)

    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    mCount = 0;
    mSum = 0
    for i in ns:
        if mCount % 2 == 0:
            mSum += 4 / i
        else:
            mSum -= 4 / i
        mCount += 1

    # 下面这种写法不行
    # listAdd = [4 / x for x in ns if x % 4 == 1]
    # print(listAdd)
    #
    # listAdd2 = [4 / x for x in ns if x % 4 == 1]
    # print(listAdd2)

    # step 4: 求和:
    return sum(listAdd) + sum(listAdd2)


# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')

# 小结
#
# itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是Iterator，只有用for循环迭代的时候才真正计算。
