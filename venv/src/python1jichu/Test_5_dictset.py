# -*- coding: utf-8 -*-

# Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。

#   dist类似于java中的set , set取值的方法有两种
#
#   第一种是  d['string']
#   第二种是  通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
#           d.get('sdf') 或者 娶不到的时候拿一个默认的 值  d.get('sdf','112')
#
#   删除方法:  pop('key')
#
#   list 就相当于 java 中的 list , 有序, 可重复
#   set 相当于 java中的 set , 无序 ,  不可重复
#
#   dist 相当于 java中的map , 无序, key 不可重复,  是键值对的集合
#
#
#   set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
#
#

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

# print(d.get("Tracy", 'hehe'))

s = set(list(range(1, 5)))
print(s)
s = set([1, 1, 1, 2, 2, 3, 3, 4])
print(s)
# print([1, 1, 1, 2, 2, 3, 3, 4])


# 可以 进行交集 并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])

sj = s1 & s2
# print(sj)

sb = s1 | s2
# print(sb)


# 可变对象和 不可变对象
a = ['c', 'b', 'a']
a.sort()
print(a)


ss1 = 10450
print(ss1/10227)





