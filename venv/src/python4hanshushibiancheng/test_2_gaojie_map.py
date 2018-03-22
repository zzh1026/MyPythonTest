#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# create by zzh
#
# Python内建了map()和reduce()函数。

# map()函数接收两个参数，一个是函数，一个是Iterable，
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

def f(x):
    return x * x


lists = list(range(1, 10))
# print(lists)

r = map(f, lists)
# print(list(r))

# print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
# map()作为高阶函数，事实上它把运算规则抽象了，因此，我们不但可以计算简单的f(x)=x2，还可以计算任意复杂的函数

#
# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# 其效果就是：
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
#
from functools import reduce


# 对一个序列求和，就可以用reduce实现：(也可以用sum() 方法直接计算)
def add(x, y):
    return x + y


# print(reduce(add, lists))
# print(sum(lists))

def fn(x, y):
    return 10 * x + y


# print(reduce(fn, lists))

# 字符串str也是一个序列，对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数：
def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


# print(reduce(fn, map(char2num, "980903485")))

# 整理成一个str2int的函数就是：
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return DIGITS[s]

    return reduce(fn, map(char2num, s))


# print(str2int("891237489"))

# 还可以用lambda函数进一步简化成：
def char2num(s):
    return DIGITS[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


#
# 总结:  map函数是 传入一个  fun 函数 和 一个list  ,然后 使用  fun对list 中的每一个元素依次进行操作,结果返回一个 iterable
#       reduce函数是传入一个 fun 函数 和 一个list ,然后使用依次对 list中的每一个元素进行操作, 结果返回普通结果
#

# 测试1:
# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
from functools import reduce


def prod(L):
    return reduce(lambda x, y: x * y, L)


# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

# 测试2:
# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}


def str2float(s):
    # nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    # point = 0
    #
    # def to_float(f, n):
    #     nonlocal point
    #     if n == -1:
    #         point = 1
    #         return f
    #     if point == 0:
    #         return f * 10 + n
    #     else:
    #         point = point * 10
    #         return f + n / point
    #
    # return reduce(to_float, nums, 0.0)
    int_part, dec_part = s.split('.')
    return reduce(lambda x, y: 10 * x + y, map(int, int_part)) + \
           reduce(lambda x, y: 10 * x + y, map(int, dec_part)) * 10 ** (-len(dec_part))


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')


# 测试3:
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，
# 输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    return name[0].upper() + name[1:].lower()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
