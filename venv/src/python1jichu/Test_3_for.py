# -*- coding: utf-8 -*-

# for循环

# Python的循环有两种，
#
# 一种是for...in循环，依次把list或tuple中的每个元素迭代出来,
# for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句。
#
#
# 第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。
# 比如我们要计算100以内所有奇数之和，可以用while循环实现：
#

name = ['hehe', 'nimeide', 'sb']

for named in name:
    print(named)

# range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数
sums = 0
for i in range(101):
    sum += i
print(sums)

# print(list(range(10)))
# print(range(10))
# print(list(range(20,41)))

sums = 0
n = 99
while n > 0:
    sums += n
    n -= 2
print(sums)

# 请利用循环依次对list中的每个名字打印出Hello, xxx!：
L = ['Bart', 'Lisa', 'Adam']
for str in L:
    print('Hello,%s' % str)
