#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 注释 '

__author__ = 'zzh'


#
# 错误处理
#
# 1, 使用try...except...finally...的错误处理机制
#       如果发生了不同类型的错误，应该由不同的except语句块处理。没错，可以有多个except来捕获不同类型的错误：
#
#   如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句：
#   所有的错误类型都继承自BaseException
#   不需要在每个可能出错的地方去捕获错误，只要在合适的层次去捕获错误就可以了。这样一来，就大大减少了写try...except...finally的麻烦。
#
# 调试方式:
# 1, 使用断言 assert ,使用方式: assert n != 0, 'n is zero!' , 如果断言失败，assert语句本身就会抛出AssertionError.
# 2, 使用日志 logging ,logging不会抛出错误，而且可以输出到文件 ,需要import logging
# 3, 使用 python调试器 pdb, 让程序以单步方式运行，可以随时查看运行状态。
#
#
def tryTest():
    try:
        print('try...')
        r = 10 / 2
        print('result:', r)
    except ValueError as e:
        print('ValueError:', e)
    except ZeroDivisionError as e:
        print('except:', e)
    else:
        print('except:', 'success')
    finally:
        print('finally...')
    print('END')


# tryTest()

#
# 2, 调用栈
# 如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出。来看看err.py：
#
# err.py:

def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    bar('0')


# main()
#  出错的时候，一定要分析错误的调用栈信息，才能定位错误的位置。

#
# 3, 记录错误
# 如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了。
# 既然我们能捕获错误，就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。
#
# Python内置的logging模块可以非常容易地记录错误信息：
import logging


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)


# main()
# print('END')


# 同样是出错，但程序打印完错误信息后会继续执行，并正常退出.通过配置，logging还可以把错误记录到日志文件里，方便事后排查

#
# 4, 抛出错误
# 要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例：
#
class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n


# foo('0')

#
# 5, 向上抛错误
#
#   raise语句如果不带参数，就会把当前错误原样抛出。此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：
#
def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n


def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise


# bar()

# 在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：
# try:
#     10 / 0
# except ZeroDivisionError:
#     raise ValueError('input error!')
#

# 练习
# 运行下面的代码，根据异常信息进行分析，定位出错误源头，并修复：
from functools import reduce


def str2num(s):
    try:
        return int(s)
    except Exception:
        try:
            return float(s)
        except Exception:
            raise ValueError('错误的参数类型 :%s ,应该为 int 或者 float 来进行计算' % s)


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)


main()

# 小结
# Python内置的try...except...finally用来处理错误十分方便。出错时，会分析错误信息并定位错误发生的代码位置才是最关键的。
# 程序也可以主动抛出错误，让调用者来处理相应的错误。但是，应该在文档中写清楚可能会抛出哪些错误，以及错误产生的原因。
