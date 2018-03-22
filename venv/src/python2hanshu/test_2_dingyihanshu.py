# -*- coding: utf-8 -*-

import math

r1 = 12.34
r2 = 9.08
r3 = 73.1


# 计算圆形面积的函数
def area_of_cricle(r):
    s = 3.14 * r * r
    return s


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')

    if x < 0:
        x = -x
    return x


def passTest():
    pass


# 参数检查  if not isinstance(x, (int, float)):

# 函数可以返回多个值吗？答案是肯定的。
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


s = area_of_cricle(r1)
print(s)

print(my_abs(-2))

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

r = move(100, 100, 60, math.pi / 6)
print(r)  # tuple函数
