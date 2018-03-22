#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 注释 '

__author__ = 'zzh'


#
# 单元测试
class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


# 单元测试，我们需要引入Python自带的unittest模块
# 编写mydict_test.py如下：
import unittest


# class TestDict(unittest.TestCase):
#
#     def test_init(self):
#         d = Dict(a=1, b='test')
#         self.assertEqual(d.a, 1)
#         self.assertEqual(d.b, 'test')
#         self.assertTrue(isinstance(d, dict))
#
#     def test_key(self):
#         d = Dict()
#         d['key'] = 'value'
#         self.assertEqual(d.key, 'value')
#
#     def test_attr(self):
#         d = Dict()
#         d.key = 'value'
#         self.assertTrue('key' in d)
#         self.assertEqual(d['key'], 'value')
#
#     def test_keyerror(self):
#         d = Dict()
#         with self.assertRaises(KeyError):
#             value = d['empty']
#
#     def test_attrerror(self):
#         d = Dict()
#         with self.assertRaises(AttributeError):
#             value = d.empty
#
#     def setUp(self):
#         print('setUp...')
#
#     def tearDown(self):
#         print('tearDown...')


# 编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承。
#
# 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。
# 最常用的断言就是assertEqual()
# 另一种重要的断言就是期待抛出指定类型的Error，比如通过d['empty']访问不存在的key时，断言会抛出KeyError：

# with self.assertRaises(KeyError):
#     value = d['empty']

# 而通过d.empty访问不存在的key时，我们期待抛出AttributeError：

# with self.assertRaises(AttributeError):
#     value = d.empty

# if __name__ == '__main__':
#     unittest.main()


# setUp与tearDown
#
# 可以在单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。

# class TestDict(unittest.TestCase):
#
#     def setUp(self):
#         print('setUp...')
#
#     def tearDown(self):
#         print('tearDown...')


# 练习
# 对Student类编写单元测试，结果发现测试不通过，请修改Student类，让测试通过：
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score > 100 or self.score < 0:
            raise ValueError
        if self.score >= 80:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


class TestStudent(unittest.TestCase):
    def test_80_to_100(self):
        s1 = Student('Bart', 80)
        s2 = Student('Lisa', 100)
        self.assertEqual(s1.get_grade(), 'A')
        self.assertEqual(s2.get_grade(), 'A')

    def test_60_to_80(self):
        s1 = Student('Bart', 60)
        s2 = Student('Lisa', 79)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_0_to_60(self):
        s1 = Student('Bart', 0)
        s2 = Student('Lisa', 59)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

    def test_invalid(self):
        s1 = Student('Bart', -1)
        s2 = Student('Lisa', 101)
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()


if __name__ == '__main__':
    unittest.main()
