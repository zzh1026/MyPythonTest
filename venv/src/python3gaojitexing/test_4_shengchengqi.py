#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# create by zzh

#
# 生成器的定义: 在Python中，这种一边循环一边计算的机制，称为生成器;  现在只有  yieid 关键字的 函数生成generator 是
#
# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
# 而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，
# 那后面绝大多数元素占用的空间都白白浪费了。
#
# 所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，
# 从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。

# 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
#
# 第二种方法是 使用 yield 来进行处理
#

L = [x * x for x in range(10)]
# print(L)

g = (x * x for x in range(10) if x % 4 < 2)
# print(g)

# 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
# 可以通过next()函数获得generator的下一个返回值
# print(next(g))  # 没有更多的元素时，抛出StopIteration的错误。一般不使用这个方法

for n in g:
    # print(n)
    pass


# 斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# 斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易：
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        # yield b
        a, b = b, a + b
        n = n + 1
    return 'success'


# print(fib(6))


# 注意，赋值语句： a, b = b, a + b 相当于：
# t = (b, a + b) # t是一个tuple
# a = t[0]
# b = t[1]
# 但不必显式写出临时变量t就可以赋值。


# generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
# 如果一个函数中有 tidid 关键字, 这个函数本身就是一个 generator 了, 所以函数内部 的return 结果是没有意义的
def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'success'


# yield b , 首先用yidid 小时该函数是 generator ,其次 b 表示 b组成的列表为 该 generator 的元素
# 这是因为: generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
# 所以 feb2 中 yieid 执行到的时候就已经返回了 generator,不会执行到return语句
f = fib2(10)
# print(f)
# print(fib2(4))
for x in f:
    # print(x)
    pass


# 举个简单的例子，定义一个generator，依次返回数字1，3，5：
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield (3)
    print('step 3')
    yield (5)


# 该generator时，首先要生成一个generator对象，然后用next()函数不断获得下一个返回值：
o = odd()
# print(o)

# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：

g = fib2(6)
# print(g)

while True:
    try:
        x = next(g)
        # print('g:', x)
    except StopIteration as e:
        # print('Generator return value:', e.value)
        break
    pass


# 练习:杨辉三角 把每一行看做一个list，试写一个generator，不断输出下一行的list：
def triangles():
    l = [1]
    while True:
        yield l
        l = [1] + [l[n] + l[n + 1] for n in range(len(l) - 1)] + [1]  # 这个很恐怖
    return


# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
