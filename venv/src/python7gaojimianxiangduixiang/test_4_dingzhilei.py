#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 注释 '

__author__ = 'zzh'


#
# 定制类
#
# 看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。
#
# __slots__ 用来限制绑定属性 使用方法 : __slots__ = ('name','age','set_source)),来对绑定的属性或者方法进行限制,但是只限制实例不限制类
#
# __len__ 用来返回 实例的长度 ,在 len(o) 的时候会调用
#
# 除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。
#
# 1, __str__ , 类似java中的 toString() 方法,相应的还有 __repr__ ,__str__()返回用户看到的字符串，
#     而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
# 2, __iter__, __next__ ,来让 类 可以实现 for ... in 循环，该方法返回一个迭代对象
# 3, __getitem__ ,__setitem__ ,__delitem__ 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法,相对应的还有set设置和del删除
# 4, __getattr__ ,__setattr__ ,__delattr__ 在没有找到属性的情况下 , 会调用 __getattr__ 的方法,如果没有重写就报错,相对应还有set属性和del属性
# 5, __call__, 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。
#       能不能直接在实例本身上调用呢？在Python中，答案是肯定的。只需要定义一个__call__()方法，就可以直接对实例进行调用。
#

# __str__
#
# 类似于java中的 toString() 方法,默认返回的是当前对象的地址值, 通过该方法定制返回值
# 解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的，所以，有个偷懒的写法：
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__


print(Student('Michael'))


# __iter__ , __next__
#
# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，
# 该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
# 直到遇到StopIteration错误时退出循环。

# 以斐波那契数列为例，写一个Fib类，可以作用于for循环：
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值


# 可以吧 Fib实例作用于for循环
for n in Fib():
    # print(n)
    pass


# __getitem__ []获取, __setitem__ []设置 , __delitem__ []删除
#
# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
class Fib(object):
    def __getitem__(self, n):
        a, b = 0, 1
        for x in range(n):
            a, b = b, a + b
        return a


f = Fib()
print(f[5])


# __getattr__
#
# 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().status.user.timeline.list)


# __call__
#
# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。
# 能不能直接在实例本身上调用呢？在Python中，答案是肯定的。
#
# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。请看示例：
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)


# 调用方式如下
s = Student('Michael')
s()  # self参数不要传入

# __call__()还可以定义参数。
# 对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。

# 判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call__()的类实例：
print(callable(Student('ksjdf')))
print(callable(max))
print(callable([1, 2, 3]))
print(callable(None))
print(callable('str'))

# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。

# 小结
# Python的class允许定义许多定制方法，可以让我们非常方便地生成特定的类。
