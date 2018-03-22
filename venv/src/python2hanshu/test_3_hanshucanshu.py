#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# create by zzh

# Python的函数定义非常简单，但灵活度却非常大。除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数，
#       使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码。
#
#   函数参数有以下几种
#       1,位置参数(必选参数)
#       2,默认参数
#       3,可变参数 (传入 list 或者 tuple , *list)
#       4,关键字参数(传入 map , **kw)
#       5,命名关键字参数(传入 def person(name, age, *, city, job): ,用*特殊分隔符进行分割 ,同时参数中不可传多余的字段,可以在其后跟
#               **kw来达到传多余字段的效果).
#       6,参数组合 (参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。)
#
#
#
#   Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
#
#   默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
#
#   要注意定义可变参数和关键字参数的语法：
#
#   *args是可变参数，args接收的是一个tuple；
#
#   **kw是关键字参数，kw接收的是一个dict。
#
#   以及调用函数时如何传入可变参数和关键字参数的语法：
#
#   可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
#
#   关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
#
#   使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
#
#   命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
#
#   定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
#


# 位置参数
# power(x, n)函数有两个参数：x和n，这两个参数都是位置参数，调用函数时，传入的两个值按照位置顺序依次赋给参数x和n。
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


# 默认参数

# print(power(185))

def enroll(name, gender, age=6, city='beijing'):
    print('name:%s' % name)
    print('gender:%s' % gender)
    print('age:%s' % age)
    print('city:%s' % city)


# enroll('zzh', 'nan')
# enroll('zzh', 'nan', '4')
# enroll('zzh', 'nan', city='shanghai')
# enroll('zzh', 'nan', age=2)


# 定义默认参数要牢记一点：默认参数必须指向不变对象！  重点:  默认参数为不可变
# 因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。
#           此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。
#           我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


# print(add_end())
# print(add_end())
# print(add_end())

def calc(*numbers):
    # if numbers is ():  # 如果是 tuple 的话
    sum = 0
    for n in numbers:
        sum += n * n
    return sum

    # else:
    #     raise TypeError("输入有误")

    # print(calc(1, 2, 3))


# *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。
nums = [1, 2, 3]


# print(calc(*nums))

# 关键字参数  *代表单个 , ** 代表 键值对

# 可变参数 主要是 tuple 和list  用* 表示 ;  关键字参数 主要是 map  ,用 ** 表示
def person(name, age, **kw):
    # print(kw.get('lele'))
    # print('name:', name, 'age:', age, 'other:', kw)
    return kw


# print(person('Michael', 30, lele='city', luelue='sldfj'))

# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，
# 注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
extra = {'city': 'Beijing', 'job': 'Engineer'}


# 命名关键字参数
# 关键字参数的调用中 , 调用者可以传入不受限制的关键字参数：

# 要限制关键字参数的名字，就可以用命名关键字参数的方式，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
def person(name, age, *, city, job):
    print(name, age, city, job)
    return


# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。

# print(person('Jack', 24, city='Beijing', job='Engineer'))

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person(name, age, *args, city='bbeijing', job='slkdjflksdf'):
    # print(name, age, args, city, job)
    return


person('zzh', 14, 1, 3, 5, city='beijing', job='hehe')


# 位置参数 -> 默认参数 -> 可变参数 -> 关键字参数
def f1(a, b, c=0, *args, **kw):
    # print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
    return


f1(1, 2)
f1(1, 2, 3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99, hehe='lele')


# 位置参数 -> 默认参数 -> 命名关键字参数 -> 关键字参数
def f2(a, b, c=0, *, d='lskdjf', k, **kw):
    # print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
    return


f2(1, 2, d=99, k='lskdjf', ext=None)
f2(1, 2, k='lll', ext=None)

# 通过一个tuple和dict，你也可以调用上述函数：(即通过 list 和 map)
args = (1, 2, 3, 4)  # 这是一个tuple
kw = {'d': 99, 'x': '#'}  # 这是一个 map ,即 dict , 字典
f1(*args, **kw)  # 相当于 f1(1,2,3,4,**kw)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#', 'k': 'lele'}
f2(*args, **kw)  # 相当于 f2(1,2,3,d=88,k=lele,x=#)
