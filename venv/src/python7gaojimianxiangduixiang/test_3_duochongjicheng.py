#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 注释 '

__author__ = 'zzh'


# 多重继承
#
# 继承是面向对象编程的一个重要的方式，因为通过继承，子类就可以扩展父类的功能。
#

# 采用多重继承的方式为:
class Animal(object):
    pass


# 大类:哺乳动物
class Mammal(Animal):
    pass


# 鸟类
class Bird(Animal):
    pass


# 各种动物:
class Dog(Mammal):
    pass


class Bat(Mammal):
    pass


class Parrot(Bird):
    pass


class Ostrich(Bird):
    pass


class Runnable(object):
    def run(self):
        print('Running...')


class Flyable(object):
    def fly(self):
        print('Flying...')


# 多继承的使用方法
#
# 对于需要Runnable功能的动物，就多继承一个Runnable，例如Dog：
class Dog(Mammal, Runnable):
    pass


class Bat(Mammal, Flyable):
    pass


# 通过多重继承，一个子类就可以同时获得多个父类的所有功能。

# MixIn
#
# 在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。
# 但是，如果需要“混入”额外的功能，通过多重继承就可以实现，
# 比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。
#
# 即非主干的 功能一般后缀加上 MixIn
#
# MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，
# 我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。


# 小结
# 由于Python允许使用多重继承，因此，MixIn就是一种常见的设计。
# 只允许单一继承的语言（如Java）不能使用MixIn的设计。

# 练习:
#
# 1.有两个基类A和B,A和B都定义了方法f(),C继承A和B,那么调用C的f()方法时会出现不确定。
# 2.有一个基类A，定义了方法f()，B类和C类继承了A类（的f()方法），D类继承了B和C类，那么出现一个问题，D不知道应该继承B的f()方法还是C的f()方法
# (第二个问题的本质是第一个问题,即两个问题本质上是一个问题)
#
# 1.
class A(object):
    def f(self):
        print("A")


class B(object):
    def f(self):
        print("B")


class C(A, B):
    pass


class D(B, A):
    pass


c = C()
d = D()
c.f()  # 会输出什么? A
d.f()  # 会输出什么? B


# "A" or "B"
# 结论:输出什么的决定性因素是C在继承父类时的顺序!
# 即靠近左边的先输出!

# 2.
class A(object):
    def f(self):
        print("A")


class B(A):
    def f(self):
        print("AB")


class C(A):
    def f(self):
        print("CB")


class D(B, C):
    pass


class E(C, B):
    pass


d = D()
e = E()
d.f()
e.f()
# 结论:输出什么的决定性因素是C在继承父类时的顺序!
# 即靠近左边的先输出!

# 结论相同: 根据继承的先后顺序来判断相同方法的时候调用那个方法,即后面类的方法不会对先继承的类的方法进行覆盖
