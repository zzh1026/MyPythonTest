#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# create by zzh

# 切片

# L取前3个元素，应该怎么做？
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']


# 方法:
def getList(n):
    r = []  # 可变list
    for i in range(n):
        r.append(L[i])
    return r


# print(getList(3))
# print(L[4:])
# print(L[-2:])
# print(L[-2:-1])


lists = list(range(99))
yy = []

# yy = lists[:10]  # 取前10个数

# yy = lists[-10:]  # 后10个数

# yy = lists[10:20]  # 前11-20个数

# yy = lists[:10:2]  # 前10个数，每两个取一个：

# yy = lists[::5]  # 所有数，每5个取一个：  :表示所有的数字  :5 表示每隔5个取一次

# yy = lists[:]  # 只写[:]就可以原样复制一个list：

# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
# tup = tuple(range(20))
# yy = tup[::3]
# print(tup)

# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：
str = "slkdjfklsdjfklsjdfkljsdklf"
yy = str[::5]


# print(yy)

# 测试: 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：

def trim(str=None):
    if str is None:
        return None
    while str[0] == ' ':
        str = str[1:]
    while str[-1] == ' ':
        str = str[:len(str) - 1]
    return str


def trim2(str=None):
    if str is None:
        return None
    str = trimStart(str)
    str = trimEnd(str)
    return str


def trimStart(str):
    if str[0] == ' ':
        return trimStart(str[1:])
    else:
        return str


def trimEnd(str):
    if str[-1] == ' ':
        return trimEnd(str[: - 1])
    else:
        return str
    pass


def trim3(str=None):
    if str is None:
        return None
    if str[0] == ' ':
        return trim3(str[1:])
    elif str[-1] == ' ':
        return trim3(str[:-1])
    else:
        return str


str2 = '   skldjflsdjflksdj dsklf sdlkfjlsdfj   '
str3 = str2.strip()
str4 = trim(str2)
str5 = trim2(str2)
str6 = trim3(str2)
print(str2)
print(str3)
print(str4)
print(str5)
print(str6)
