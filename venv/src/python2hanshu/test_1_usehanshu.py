# -*- coding: utf-8 -*-

# 调用函数

r1 = 12.34
r2 = 9.08
r3 = 73.1

# s = area_of_cricle(r1)

# print(abs(1))

# print(max(1,2,3,4,-1,8,4))


# 数据类型转换 , Python内置的常用函数还包括数据类型转换函数，比如int()函数可以把其他数据类型转换为整数：

print(int('123'))
print(int(12.34))
print(float('12.34'))
print(str(12.34))
print(str(100))
print(bool(1))
print(bool(4 > 3))

n1 = 255
n2 = 1000

print('%s的十六进制为%s,\n%s的十六进制为%s' % (n1, hex(n1), n2, hex(n2)))
