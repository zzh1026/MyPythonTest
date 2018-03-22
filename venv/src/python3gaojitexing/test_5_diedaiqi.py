#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# create by zzh
#
# 可以直接作用于for循环的数据类型有以下几种
#
# 一类是集合数据类型，如list、tuple、dict、set、str等；
# 一类是generator，包括生成器和带yield的generator function。
#
# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
#
# 可以使用isinstance()判断一个对象是否是Iterable对象：
#

from collections import Iterable

# print(isinstance([], Iterable))  # list
#
# print(isinstance((), Iterable))  # tuple
#
# print(isinstance({}, Iterable))  # dict
#
# print(isinstance("abe", Iterable))  # str
#
# print(isinstance([x for x in range(10)], Iterable))  # [] 为 list
#
# print(isinstance((x for x in range(10)), Iterable))  # () gener
#
# print(isinstance(set([]), Iterable))  # set
#
# print(isinstance(100, Iterable))  # int 不是 Iterable 对象

#
#
# 而生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了。
#
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
#
# 可以使用isinstance()判断一个对象是否是Iterator对象：
#

from collections import Iterator

# print(isinstance((x for x in range(10)), Iterator))  # gener
#
# print(isinstance([], Iterator))  # list 不是 Iterator
#
# print(isinstance({'123': 'ksdfj', 'slkdf': 'skdlfj'}, Iterator))  # dict 不是 Iterator
#
# print(isinstance('abc', Iterator))  # str 不是 Iterator

#
# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
#

#
# 可以把list、dict、str等Iterable变成Iterator可以使用iter()函数：
#

# print(isinstance(iter([]), Iterator))  # 通过 iter 方法将list变成 Iterator
#
# print(isinstance(iter('abc'), Iterator))  # 通过 iter 方法将str变成 Iterator

#
#
# 为什么list、dict、str等数据类型不是Iterator?
#
# 这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，
# 直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，
# 只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
#
# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。
#

#
# 小结:
#
#  1, 凡是可作用于for循环的对象都是Iterable类型；
#  2, 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
#  3, 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
#  4, Python的for循环本质上就是通过不断调用next()函数实现的
#
for x in [1, 2, 3, 4, 5]:
    # print(x)
    pass
# 实际上完全等价于：

# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break

# 测试
d = {'a': 1, 'b': 2, 'c': 3}

# iter each key:
for k in d.keys():
    # print('key:', k)
    pass

# iter each value:
for v in d.values():
    # print('value:', v)
    pass

# iter both key and value:
for k, v in d.items():
    # print('item:', k, v)
    pass

# iter list with index:
for i, value in enumerate(['A', 'B', 'C']):  # 将list 拆成  下标和 value 的类 dict组合并取出
    # print(i, value)
    pass

# iter complex list:
for x, y in [(1, 1), (2, 4), (3, 9)]:  # 一个list ,元素为 tuple
    # print(x, y)
    pass

a = [(1, 1), (2, 4), (3, 9)]
for x in a:
    # print(x[1])
    pass
