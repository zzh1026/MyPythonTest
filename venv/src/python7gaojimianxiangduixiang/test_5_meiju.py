#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 注释 '

__author__ = 'zzh'

# 使用枚举类
#
# 枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例。Python提供了Enum类来实现这个功能：
from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Nov', 'Dec'))

# 这是简单的定义enum 的方法
# 这样我们就获得了Month类型的枚举类，可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员：
print(Month.Jan)

for name, number in Month._member_map_.items():
    # print('name->', name, ' and number->', number)
    pass

# value属性则是自动赋给成员的int常量，默认从1开始计数。 这种定义方式不好用

# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
from enum import Enum, unique


# @unique装饰器可以帮助我们检查保证没有重复值。
@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    # Fri = 5
    Sat = 6


# 访问这些枚举类型可以有若干种方法：

# 1 , 使用 Weekday.Mon 直接获取
print(Weekday.Thu)

# 2 , 使用list[] 的方式获取 ,Weekday['Tue']
print(Weekday['Tue'])

# 3 , 获取 value值 print(Weekday.Tue.value)
print(Weekday.Tue.value)

# 4 , 通过value 的方式获取  Weekday(1)
print(Weekday(6))


# 枚举既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量。

# 练习
# 把Student的gender属性改造为枚举类型，可以避免使用字符串：
@unique
class Gender(Enum):
    Male = 0
    Female = 1


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = Gender(gender)


# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')

# 小结
#
# Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较。
