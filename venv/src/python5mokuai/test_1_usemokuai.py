#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# create by zzh
#
# 使用模块
#
# Python本身就内置了很多非常有用的模块，只要安装完毕，这些模块就可以立刻使用。
#
#
'这是一个注释'
__author__ = 'zzh'

import sys


def test():
    args = sys.argv
    print(args)
    if len(args) == 1:
        print('hello ,world')
    elif len(args) == 2:
        print('hello , %s' % args[1])
    else:
        print('too many arguments')
    return


# 当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，
# if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
#
# 在使用 import xxx模块的时候会先将 xxx模块执行代码 , 所以 这个时候使用 if __name__ == '__main__': 来测试更好
#
# 总结: 导入 不会执行  __name__ == '__main__' 中的代码, 直接运行该文件才会执行


#
# 作用域
#
# 在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用。
# 在Python中，是通过_前缀来实现的。
#
#
# 正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等；
#
# 类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，
#       hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名；
#
# 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；
#
# 之所以我们说，private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，
# 是因为Python并没有一种方法可以完全限制访问private函数或变量，但是，从编程习惯上不应该引用private函数或变量。

# private函数或变量不应该被别人引用，那它们有什么用呢？请看例子：
def _private_1(name):  # _xxx类型,代表 private, 不应该被直接引用
    return 'Hello, %s' % name


def _private_2(name):
    return 'Hi, %s' % name


def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
    pass


# 我们在模块里公开greeting()函数，而把内部逻辑用private函数隐藏起来了，
# 这样，调用greeting()函数不用关心内部的private函数细节，这也是一种非常有用的代码封装和抽象的方法，即：
#
# 外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。

if __name__ == '__main__':
    print('执行了')
    test()
    print(greeting('市劳动纠纷'))
    pass
