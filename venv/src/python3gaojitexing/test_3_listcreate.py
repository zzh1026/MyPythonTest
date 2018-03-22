#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# create by zzh

# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
# 主要介绍list 的生成方式
#
#
# 创建 list 集合的表达式 为
# L = [*x(包含有*x的表达式,可以不止一个) for *x(对应前面的*x来保证前面的表达式能运行) in list(通过简单的list创建复杂的list) if *x(对list进行筛选)]
# .

# 生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list = tuple(range(1, 11))
# list = list(range(1, 11))
# print(list)

# 要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？
# 方法一是使用循环
L = []
for x in range(1, 11):
    L.append(x * x)
    pass
# print(L)

# 循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list：
L = ['%s * %s = %s' % (x, x, x * x) for x in range(1, 11)]  # 首先使用 [] 表示 集合 ,其次生成列表 ,并对x进行运算
# print(L)

# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来。
# for循环后面还可以加上if判断，这样我们就可以对list进行筛选：
L = [x * x for x in range(1, 11) if x % 2 == 0]
# print(L)

# 还可以使用两层循环，可以生成全排列：
L = [m + n for m in 'ABC' for n in 'XYZ']
# L = [m + n + o for m in 'ABC' for n in 'XYZ' for o in '123']
# print(L)

# 运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
import os  # 导入os模块，模块的概念后面讲到

L = [d for d in os.listdir('C:/Users/zhaozehui/Desktop/Shadowsocks-4.0.7')]  # os.listdir可以列出文件和目录
# print(L)

# print(os.cpu_count())

# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    # print(k, v)
    pass

lists = [k + '=' + v for k, v in d.items()]
# print(lists)

L = ['Hello', 'World', 'IBM', 'Apple']
S = [str.lower() for str in L]
# print(S)


# 练习:如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
# 使用内建的isinstance函数可以判断一个变量是不是字符串：
# 请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
L = ['Hello', 'World', 18, 'Apple', None]
# print([s.lower() for s in L])#这样会报错, 因为 18 没有 lower()方法
L2 = [item.lower() for item in L if isinstance(item, str)]
# print(result)

# 测试
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
