#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 注释 '

__author__ = 'zzh'

#
# 文件读写
#
#
# 读文件
# 要以读文件的模式打开一个文件对象，使用Python内置的open()函数，传入文件名和标示符：
f = open('C:/Users/zhaozehui/Desktop/pythontest.txt', 'r')
# print(f.read())
f.close()

#
# 其使用过程是:
#       1, 打开文件, 用open
#       2, 读取文件, 用read方法
#       3, 关闭文件, 释放资源 , 使用 close 方法
#
# 由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。
# 所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现
try:
    f = open('C:/Users/zhaozehui/Desktop/pythontest.txt', 'r')
    # print(f.read())
finally:
    if f:  # 这里的if f相当于 if != None ,表示如果不为空
        f.close()

# 但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：
# 所以不仅可以使用 open 方法,但是需要手动关闭,也可以使用 with方法来自动关闭
with open('C:/Users/zhaozehui/Desktop/pythontest.txt', 'r') as f:
    # print(f.read(), '==>', 'OVER')
    pass

# 这和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。

# read()会一次性读取文件的全部内容
# 一般都是 反复调用read(size)方法, 每次最多读取size个字节的内容
# 也可以 调用readline()可以每次读取一行内容
# 还可以 调用readlines()一次读取所有内容并按行返回list
#
# 如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：
with open('C:/Users/zhaozehui/Desktop/error.log', 'r') as f:
    for line in f.readlines():
        # print(line.strip())
        pass

# file-like Object
#
# 像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。(类文件对象)

# 二进制文件(使用 'rb' 模式打开)
#
# 要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：
with open('C:/Users/zhaozehui/Desktop/login.png', 'rb') as f:
    # print(f.read(6))
    pass

#
# 字符编码
#
# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：
# 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。
# 遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略
# with open('C:/Users/zhaozehui/Desktop/161337.txt', 'rb', encoding='gbk', errors='ignore'):
#     f.readline()
#     pass

#
# 写文件
# 写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：
with open('C:/Users/zhaozehui/Desktop/pythontest.txt', 'a') as f:
    # print(f.write('黑凤梨.路上看到警方时代峰峻克里斯多夫金坷垃....'))
    pass

# 以'w'模式写入文件时，如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）。
# 如果我们希望追加到文件末尾怎么办？可以传入'a'以追加（append）模式写入。

# 练习
# 请将本地一个文本文件读为一个str并打印出来：
fpath = r'C:\Windows\system.ini'
with open(fpath, 'r') as f:
    result = ''
    for line in f.readlines():
        result += line.strip()
    print(result)
    pass

# 小结
# 在Python中，文件读写是通过open()函数打开的文件对象完成的。使用with语句操作文件IO是个好习惯。


from datetime import datetime

with open('test.txt', 'w') as f:
    f.write('今天是 ')
    f.write(datetime.now().strftime('%Y-%m-%d %H-%M-%S'))
    print(datetime.now())

with open('test.txt', 'r') as f:
    s = f.read()
    print('open for read...')
    print(s)

with open('test.txt', 'rb') as f:
    s = f.read()
    print('open as binary for read...')
    print(s)
