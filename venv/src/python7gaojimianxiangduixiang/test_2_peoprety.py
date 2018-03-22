#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 注释 '

__author__ = 'zzh'


# 使用@property
#
# Python内置的@property装饰器就是负责把一个方法变成属性调用的：
# @property的作用是可以 既检查参数，又可以用类似属性这样简单的方式来访问类的变量
#
# 在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改：
class Student(object):
    def get_score(self):
        return self.__score

    def set_score(self, score):
        if not isinstance(score, int):
            raise ValueError('分数必须是整数')
        if score < 0 or score > 100:
            raise ValueError('分数必须在 0~100 之间')
        self.__score = score


s = Student()
s.set_score(50)
print(s.get_score())


# s.set_score(244)

class Student(object):

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self.__score = value


# @property的实现比较复杂，我们先考察如何使用。
# 1 , 把一个getter方法变成属性，只需要加上@property就可以了，
# 此时，@property本身又创建了另一个装饰器@score.setter，
# 负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作
#
# 这里的setter方法和getter方法的名称是一样的 , 使用 @property 装饰的函数为get 方法, 使用 @函数名.setter 装饰的方法为set方法
s = Student()
s.score = 60  # OK，实际转化为s.set_score(60)
print(s.score)  # OK，实际转化为s.get_score()


# s.score = 9999


# 注意到这个神奇的@property，我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的。

# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
class Student(object):

    @property
    def birth(self):
        return self.__birth

    @birth.setter
    def birth(self, value):
        self.__birth = value

    @property
    def age(self):
        return self.__age


# 上面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。

# 小结
# @property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。

# 练习
# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
class Screen(object):

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, (int, float)):
            raise ValueError('width type must be int or float')
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, (int, float)):
            raise ValueError('height type must be int or float')
        self.__height = height

    @property
    def resolution(self):
        return self.__width * self.__height


# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

s.height = 23.45


class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('width must be intenger')
        if value < 0:
            raise ValueError('value must >0')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('height must be intenger')
        if value < 0:
            raise ValueError('value must be >0')
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height


s = Screen()
s.width = 10
s.height = 10
print(s.resolution)
