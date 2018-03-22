#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 注释 '

__author__ = 'zzh'


#
# 继承和多态
#
# 在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），
# 而被继承的class称为基类、父类或超类（Base class、Super class）。
#

# 比如，我们已经编写了一个名为Animal的class，有一个run()方法可以直接打印：
#
# 继承的好处: 1, 可以获得父类的全部功能
#           2, 可以有选择的对代码进行改进
#
# 多态的好处: 只需要传入父类,即限定上限即可 ,调用方只管调用，不管细节，而当我们新增一种Animal的子类时，
#           只要确保run()方法编写正确，不用管原来的代码是如何调用的。
#
#           对扩展开放：允许新增父类的子类；
#           对修改封闭：不需要修改依赖父类的所有函数函数。
#
#
#
# 覆盖: 当子类和父类存在相同的方法时,就会自动将父类的方法进行覆盖
#
class Animal(object):
    def run(self):
        print('Animal is running...')


# 当我们需要编写Dog和Cat类时，就可以直接从Animal类继承：
class Dog(Animal):
    def run(self):
        print('Dog is running...')

    pass


class Cat(Animal):
    def run(self):
        print('Cat is running...')

    pass


# 对于Dog来说，Animal就是它的父类，对于Animal来说，Dog就是它的子类。Cat和Dog类似。

# 继承有什么好处？最大的好处是子类获得了父类的全部功能。由于Animial实现了run()方法，
# 因此，Dog和Cat作为它的子类，什么事也没干，就自动拥有了run()方法：
dog = Dog()
# dog.run()

cat = Cat()


# cat.run()

#
# 静态语言 vs 动态语言
#
# 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
#
# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：
#
class Timer(object):
    def run(self):
        print('Start...')


# 这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
#
# Python的“file-like object“就是一种鸭子类型。对真正的文件对象，它有一个read()方法，返回其内容。
# 但是，许多对象，只要有read()方法，都被视为“file-like object“。
# 许多函数接收的参数就是“file-like object“，你不一定要传入真正的文件对象，完全可以传入任何实现了read()方法的对象。
#
# 归根结底的原因是 python中的 参数是动态语言, 不像java中的限定  test(Animal animal) ,python中是 test(animal)这个
#       animal 实际上是个变量,一个名称,所以只要有 run() 方法的对象都可以, 但是如果没有润方法会报错
#
def test(animal):
    animal.run()


class B(object):
    pass


test(Animal())
test(Dog())
test(Cat())
test(Timer())
test(B())  # AttributeError: 'B' object has no attribute 'run'

#
# 小结
# 继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。
# 动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。
#
