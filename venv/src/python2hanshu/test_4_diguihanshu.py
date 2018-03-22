#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# create by zzh
#
#
#   递归函数
#
#   在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。
#
#   解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的
#
#   尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。 (即直接调用自身本身)
#       这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，
#       都只占用一个栈帧，不会出现栈溢出的情况。
#
#
# .

# 利用递归函数计算阶乘
# N! = 1 * 2 * 3 * ... * N
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n - 1)

def fact(n):
    return fact_iter(n, 1)


# return fact_iter(num - 1, num * product)仅返回递归函数本身，num - 1和num * product在函数调用前就会被计算，不影响函数调用。
def fact_iter(num, pro):
    if num == 1:
        return pro
    return fact_iter(num - 1, num * pro)


# print(fact(9000))

# move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法，例如：
def move(n, a, b, c):
    if n == 1:  # 只有一个时，直接从a移动到c
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)  # 先将a上除了最大底盘外的所有圆盘(n-1个)移动到b
        move(1, a, b, c)  # 再将a上的最大底盘移动到c
        move(n - 1, b, a, c)  # 最后将b上的所有圆盘(n-1个)移动到c


move(5, 'A', 'B', 'C')
