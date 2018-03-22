#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 注释 '

__author__ = 'zzh'


#
# contextlib
#
# 任何对象，只要正确实现了上下文管理，就可以用于with语句, with可以实现自动管理
# 实现上下文管理是通过__enter__和__exit__这两个方法实现的。例如，下面的class实现了这两个方法：
class Query(object):
    def __init__(self, name):
        self.name = name
        print('init')

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('query in fo about %s...' % self.name)


# 这样我们就可以把自己写的资源对象用于with语句
# with Query('zzh') as q:
#     print(q.query())
#     pass

# @contextmanager
# 编写__enter__和__exit__仍然很繁琐，因此Python的标准库contextlib提供了更简单的写法，上面的代码可以改写如下：
from contextlib import contextmanager


class Querys(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)


@contextmanager
def create_query(name):
    print('Begin')
    q = Querys(name)
    yield q
    print('End')


with create_query('Bob') as q:
    q.query()

# 很多时候，我们希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现。
#
# 代码的执行顺序是：
#   1, with语句首先执行yield之前的语句
#   2, yield调用会执行with语句内部的所有语句
#   3, 最后执行yield之后的语句
#
# @contextmanager让我们通过编写generator来简化上下文管理

#
# @closing
# 如果一个对象没有实现上下文，我们就不能把它用于with语句。这个时候，可以用closing()来把该对象变为上下文对象。
# 例如，用with语句使用urlopen()：
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.baidu.com/')) as page:
    for line in page:
        print(line)
