#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 注释 '

__author__ = 'zzh'


# 面向对象编程
#
# 面向对象编程——Object Oriented Programming，简称OOP，是一种程序设计思想。OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。



class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s同学的成绩为:%s' % (self.name, self.score))


bart = Student('bart', 50)
lisa = Student(name='Lisa Simpson', score=87)

bart.print_score()
lisa.print_score()

# 面向对象的设计思想是从自然界中来的，因为在自然界中，类（Class）和实例（Instance）的概念是很自然的。
# Class是一种抽象概念，比如我们定义的Class——Student，是指学生这个概念，而实例（Instance）则是一个个具体的Student，
# 比如，Bart Simpson和Lisa Simpson是两个具体的Student。

# 所以，面向对象的设计思想是抽象出Class，根据Class创建Instance。

# 面向对象的抽象程度又比函数要高，因为一个Class既包含数据，又包含操作数据的方法。
