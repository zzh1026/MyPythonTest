#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 注释 '

__author__ = 'zzh'

#
# collections
#
# collections是Python内建的一个集合模块，提供了许多有用的集合类。

# namedtuple
#
# namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
# 自定义的这个 对象是一个 tuple 的子类, 即自定义的 tuple
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
# print(p.x)

# 用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。
#
# 类似的，如果要用坐标和半径表示一个圆，也可以用namedtuple定义：
# namedtuple('名称', [属性list]):
Circle = namedtuple('Circle', ['x', 'y', 'r'])

#
# deque : deque(list)
#
# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
from collections import deque

q = deque(['a', 'b', 'c'])
# print(q)
q.append('d')
# print(q)
q.appendleft('e')
# print(q)
# deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。

#
# defaultdict
#
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
from collections import defaultdict

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
# print(dd['key1'])  # key1存在

# print(dd['key2'])  # key2不存在，返回默认值

# 默认值是调用函数返回的，而函数在创建defaultdict对象时传入。除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。

#
# OrderedDict
#
# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
# 如果要保持Key的顺序，可以用OrderedDict：
from collections import OrderedDict

d = dict([('a', 1), ('b', 2), ('c', 3)])  # dict的Key是无序的
print(d)

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])  # OrderedDict的Key是有序的
print(od)

#
# Counter
#
# Counter是一个简单的计数器，例如，统计字符出现的个数：
from collections import Counter

c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1

print(c)
# Counter实际上也是dict的一个子类，上面的结果可以看出，字符'g'、'm'、'r'各出现了两次，其他字符各出现了一次。
#
# Counter 类可以直接调用其构造方法，传入要统计的字符串
d = Counter('programming')
print(d)

# Counter可以直接使用dict()方法转换成dict
di = dict(Counter('programming'))
print(di)

# 取最多的前3项：
c = Counter('abscsdsd').most_common(3)
print(c)


# 自己实现一个可以统计的 dict，最简单的做法是重写 __mission__ 方法：
class Counter(dict):
    def __missing__(self, key):
        return 0


c = Counter()
for ch in "hello world!":
    c[ch] += 1

print(c)

# 小结
# collections模块提供了一些有用的集合类，可以根据需要选用。
