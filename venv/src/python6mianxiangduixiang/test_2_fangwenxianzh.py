#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 注释 '

__author__ = 'zzh'


# 访问限制
# 在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑。
#
# _ 或者 __ 开头 并且 结尾 不是_或__则代表是private , 类的外部无法调用
# _ 或者__ 开头并且 以 _或__结尾的表示常量 , 可以被引用, 一般用来标记特殊量
#

class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def set_name(self, name):
        self.__name = name


# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，
# 实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问

bart = Student('Bart Simpson', 59)
bart.print_score()

# 需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，
# 不是private变量，所以，不能用__name__、__score__这样的变量名。
#
# 有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，
# 意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
#

# 双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。
# 不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量：

# print(bart._Student__name)

# 但是不同版本的Python解释器可能会把__name改成不同的变量名。

# 一种错误写法：
bart = Student('Bart lalalla', 59)
print(bart.get_name())

bart.__name = 'New Name'
print(bart.__name)

print(bart.get_name())

bart._Student__name = "New Name2"
print(bart.get_name())


# 表面上看，外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name变量不是一个变量！
# 内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量。

# 练习
# 请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender == 'male' or gender == 'female':
            self.__gender = gender
        else:
            raise ValueError("参数错误,不能使用%s来作为参数,只能使用 male 或者 female(注意大小写)" % gender)


# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('Female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
