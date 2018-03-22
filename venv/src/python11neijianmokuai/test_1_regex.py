#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 注释 '

__author__ = 'zzh'

#
# 正则表达式
#
# 在正则表达式中，如果直接给出字符，就是精确匹配。
#
#   1,\d ,数字
#   2,\w ,字母或者数字
#   3, . ,任意字符
#   4,\s ,空格
#
# 用\d可以匹配一个数字，\w可以匹配一个字母或数字,所以：
#       '00\d'可以匹配'007'，但无法匹配'00A'
#       '\d\d\d'可以匹配'010'；
#       '\w\w\d'可以匹配'py3'；
#
# .可以匹配任意字符，所以：
#       'py.'可以匹配'pyc'、'pyo'、'py!'等等。
#
#   要匹配变长的字符，在正则表达式中
#        * 表示任意个字符（包括0个）
#        + 表示至少一个字符
#        ? 表示0个或1个字符
#        {n} 表示n个字符
#        {n,m} 表示n-m个字符
#
#  \d{3}\s+\d{3,8} , 解读为:
#   1 , \d{3}表示匹配3个数字，例如'010'；
#   2 , \s 可以匹配一个空格（也包括Tab等空白符），所以\s+表示至少有一个空格，例如匹配' '，'    '等；
#   3 , \d{3,8}表示3-8个数字，例如'1234567'。
#   综合起来，上面的正则表达式可以匹配以任意个空格隔开的带区号的电话号码。
# 如果要匹配'010-12345'这样的号码,由于'-'是特殊字符，在正则表达式中，要用'\'转义，所以，上面的正则是\d{3}\-\d{3,8}。


# 进阶
#
# 要做更精确地匹配，可以用[]表示范围，比如：
#   [0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线；
#   [0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'Py3000'等等；
#   [a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量；
#   [a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）。
#
# A|B可以匹配A或B，所以(P|p)ython可以匹配'Python'或者'python'。
# ^表示行的开头，^\d表示必须以数字开头。
# $表示行的结束，\d$表示必须以数字结束。
#
# 例如: py也可以匹配'python'，但是加上^py$就变成了整行匹配，就只能匹配'py'了。  只能以 py开始, 只能以 py结尾
#


# re模块
#
# Python提供re模块，包含所有正则表达式的功能。由于Python的字符串本身也用\转义，所以要特别注意：
s = 'ABC\\-001'  # Python的字符串

# 对应的正则表达式字符串变成：
# 'ABC\-001'
# 所以一般正则表达式 的 regex 会用 r'' 的形式表示,Python的r前缀不用考虑转义的问题
s = r'ABC\-001'  # Python的字符串,对应的正则表达式字符串不变,'ABC\-001'

# 判断正则表达式是否匹配：
import re

r = re.match(r'^\d{3}\-\d{3,8}$', '010-683')
# print(r)

# print(re.match(r'[P|p]ython', 'Python'))
# print(re.match(r'.*\.com$', 'a.lsdjkm.comdsfk'))

r = re.match(r'^\d{3}-\d{3,8}$', '010-12345')
# print(r)

# match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None。常见的判断方法就是：
test = '用户输入的字符串'
if re.match(r'字符串', test):
    # print('ok')
    pass
else:
    # print('failed')
    pass

#
# 切分字符串
#
# 正则表达式切分字符串比用固定的字符更灵活
s = 'a b   c'
l = re.split(r'\s+', s)  # 至少一个数量的空格
# print(l)

s2 = 'a,b, c  d'
l2 = re.split(r'[\s\,]+', s2)  # []表示里面是或者的关系,即至少一个空格或至少一个,
print(l2)

s3 = 'a,b;; c  d'
l3 = re.split(r'[\s\,\;]+', s3)  # []表示里面是或者的关系,即至少一个空格或至少一个,
# print(l3)


#
# 分组 ,用() 来表示分组
#
# 除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组（Group）。比如：
# ^(\d{3})-(\d{3,8})$分别定义了两个组，可以直接从匹配的字符串中提取出区号和本地号码：
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.groups())
# print(m.group(0))
# print(m.group(1))
# print(m.group(2))

# 如果正则表达式中定义了组，就可以在Match对象上用group()方法提取出子串来。
# group(0)永远是原始字符串，group(1)、group(2)……表示第1、2、……个子串。
# 提取子串非常有用。例如:
t = '19:05:30'
m = re.match(
    r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])'
    r'\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
# print(m.groups())

# 这个正则表达式可以直接识别合法的时间。但是有些时候，用正则表达式也无法做到完全验证，比如识别日期：
# '^(0[1-9]|1[0-2]|[0-9])-(0[1-9]|1[0-9]|2[0-9]|3[0-1]|[0-9])$'

#
# 贪婪匹配
#
# 正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符。举例如下，匹配出数字后面的0：

# print(re.match(r'^(\d+)(0*)$', '102300').groups())

# 由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了。
# 必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配：

# print(re.match(r'^(\d+?)(0*)$', '102300').groups())

# 编译
#
# 当我们在Python中使用正则表达式时，re模块内部会干两件事情：
#       1, 编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
#       2, 用编译后的正则表达式去匹配字符串。
# 如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了，直接匹配：
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')  # 编译:
re_telephone.match('010-12345').groups()  # 使用：
re_telephone.match('010-8086').groups()  # 继续使用


# 编译后生成Regular Expression对象，由于该对象自己包含了正则表达式，所以调用对应的方法时不用给出正则字符串。

# 练习
#
# 请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：
def is_valid_email(addr):
    regex = r'[0-9a-zA-Z.]+@[0-9a-zA-Z\.]+(\.com)$'
    return re.match(regex, addr)


# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')


# 版本二可以提取出带名字的Email地址：
def name_of_email(addr):
    regex = r'<([\w\s]+)>'
    regex2 = r'([\w\s]+)@'
    result = ''
    r1 = re.match(regex, addr)
    r2 = re.match(regex2, addr)
    if r1:
        print(r1.group(1))
        result = r1.group(1)
    elif r2:
        print(r2.group(1))
        result = r2.group(1)
    return result


# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
