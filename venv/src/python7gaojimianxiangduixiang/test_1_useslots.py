#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 注释 '

__author__ = 'zzh'


#
# 使用__slots__
#
# slots的所用是 限制实例的属性
#
# 一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。先定义class：
class Student(object):
    pass


# 绑定属性
s = Student()
# print(s.name)  # 未绑定之前直接调用会报错
s.name = 'Michael'  # 动态给实例绑定一个属性
print(s.name)


# 还可以尝试给实例绑定一个方法：
def set_age(self, age):  # 定义一个函数作为实例方法
    self.age = age


from types import MethodType

s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法
s.set_age(24)  # 调用实例方法
print(s.age)  # 测试结果


# 但是，给一个实例绑定的方法，对其他实例是不起作用的,因为对某个实例绑定的数据不会影响到其他实例

# 因此,为了给所有实例都绑定方法，可以给class绑定方法：(这里其实可以同构继承来实现)(给class绑定方法的意义在于可以动态的添加class中的方法)
def set_score(self, score):
    self.score = score


Student.set_score = set_score


# 给class绑定方法后，所有实例均可调用：

# 通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。

# 使用__slots__
#
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：

class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


s = Student()  # 创建新的实例
s.name = 'Michael'  # 绑定属性'name'
s.age = 25  # 绑定属性'age'

try:
    s.score = 99
except AttributeError as e:
    print('AttributeError:', e)


# 由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。
# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
class GraduateStudent(Student):
    pass


g = GraduateStudent()
g.score = 9999


# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。

class People(object):
    __slots__ = ('name', 'score', 'set_age')


def set_age(self, age):
    print('My age is 18')


p = People()
p.name = 'Wang'
p.score = 90
from types import MethodType

p.set_age = MethodType(set_age, p)  # 这是给实例绑定方法,受到 slots的限制

# People.set_age = set_age  # 这是给 类 绑定方法 ,不受 slots 的限制
p.set_age(23)
