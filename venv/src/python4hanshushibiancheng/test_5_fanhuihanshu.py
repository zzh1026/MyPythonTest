#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# create by zzh

#
# 返回函数
# 函数作为返回值
#
# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
def calc_sum(*args):
    ax = 0
    for x in args:
        ax += x
    return ax


# print(calc_sum(1, 2, 3, 5, 6, 5, 8))

def lazy_sum(*args):
    def sum():
        ax = 0
        for x in args:
            ax += x
        return ax

    return sum


# 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：
f = lazy_sum(2, 4, 5, 6)
# print(f)
# f = <function lazy_sum.<locals>.sum at 0x0525BF18>

# 调用函数f时，才真正计算求和的结果：
b = f()
# print(b)
# b = 17

# 在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。

# 当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)


# print(f1)
# print(f2)

#
# 闭包
#
# 注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，
# 所以，闭包用起来简单，实现起来可不容易。
#

# 需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行。我们来看一个例子：
#
# 可以这样理解: 在内部定义f() 的时候并不会执行,因为这个f是定义的 ,而没有执行,因此 fs中添加的是三个不同的 f() 函数, 当调用的时候,会各自执行
# i*i 的结果, 因为 i值会刷新, 所以每个方法中保存的 i值都为3 ,所以结果都是9 , 也就是说 不调用 f() 的时候 不会执行 i*i 的结果
#
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()


# print(f1)
# print(f2)
# print(f3)
# print(f1())
# print(f2())
# print(f3())
# 在上面的例子中，每次循环，都创建了一个新的函数，然后，把创建的3个函数都返回了。
# 由于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。

#
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。(因为后续发生变化后会对结果产生影响,一定要使用固定值)
#

# 如果一定要引用循环变量怎么办？即最终使用的 是 另一个定量, 而非循环的变量
# 方法是再创建一个函数，
# 用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count():
    def f(j):
        def g():  # 这里 在 g方法中使用了 f方法中的参数, 即为 闭包
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # 此时的i已经执行 , f(j)中已经保存了 这个值, 即 存的是 i指代的这个值 而非 i这个变量
    return fs


f1, f2, f3 = count()


# print(f1())
# print(f2())
# print(f3())


# 缺点是代码较长，可利用lambda函数缩短代码。

# 练习
# 利用闭包返回一个计数器函数，每次调用它返回递增整数：

def createCounter():
    a = 0

    def counter():
        nonlocal a  # 非局部变量
        a = a + 1
        return a

    return counter


def createCounter2():
    def g():
        n = 1
        while True:
            yield n
            n = n + 1

    it = g()

    def counter():
        return next(it)

    return counter


# 测试:
counterA = createCounter2()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter2()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
