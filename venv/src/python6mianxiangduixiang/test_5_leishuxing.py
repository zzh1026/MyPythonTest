#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 注释 '

__author__ = 'zzh'


#
# 实例属性和类属性
#
# 由于Python是动态语言，根据类创建的实例可以任意绑定属性。
#

# 给实例绑定属性的方法是通过实例变量，或者通过self变量：
#
# 即通过self或者 通过实例本身进行绑定的属性都属于实例属性
# 直接在class中定义属性，这种属性是类属性，归类所有
#
class Student(object):
    def __init__(self, name):
        self.name = name


s = Student('Bob')
s.score = 90


# 定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到。
class Student(object):
    name = 'Student'


s = Student()  # 创建实例s
print(s.name)  # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
print(Student.name)  # 打印类的name属性
s.name = 'Michael'  # 给实例绑定name属性,此时,已经给实例进行了name属性的绑定,所以直接取了实例属性的name而不是类的name属性
print(s.name)  # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(Student.name)  # 但是类属性并未消失，用Student.name仍然可以访问
del s.name  # 如果删除实例的name属性,此时实例的name属性没有了,只剩下了类的name属性
print(s.name)  # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了


# 在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，
# (准确说不是屏蔽,而是获取实例的属性的时候会优先获取实例属性,当实例属性没有的时候才会去获取类的属性)
# 但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。

# 练习
# 为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：
class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1


# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')

# 小结
#
# 实例属性属于各个实例所有，互不干扰；
#
# 类属性属于类所有，所有实例共享一个属性；
#
# 不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。
