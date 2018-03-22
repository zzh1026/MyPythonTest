#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 注释 '

__author__ = 'zzh'

#
# 操作文件和目录
#
# Python内置的os模块也可以直接调用操作系统提供的接口函数。
import os

# print(os.name)  # nt

# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。

# 环境变量
#
# 在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看：

# print(os.environ['ADB'])

# 要获取某个环境变量的值，可以调用os.environ.get('key')：返回的是一个 dict的方式获取 如: dict['key'], dict.get('key')等.

#
# 操作文件和目录
#
# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：

# 查看当前目录的绝对路径: .代表绝对当前目录
# print(os.path.abspath('.'))

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# print(os.path.join('C:/Users/zhaozehui/Desktop', 'testdir'))

# 然后创建一个目录:
# print(os.mkdir('C:/Users/zhaozehui/Desktop/testdir'))

# 删掉一个目录:
# print(os.rmdir('C:/Users/zhaozehui/Desktop/testdir'))

# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。
# 要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
# print(os.path.split('/Users/michael/testdir/file.txt'))

# os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：返回一个 tuple , tuple[1] 则为 扩展名
# print(os.path.splitext('/path/to/file.txt'))

# 这些合并、拆分路径的函数并不要求目录和文件真实存在，它们只对字符串进行操作。

# 对文件重命名
# os.rename('test.text', 'test.py')

# 删掉文件:
# os.remove('test.py')
# os.mkdir('test.text')
# os.rmdir('test.text')
with open('test.text', 'w') as f:
    f.write('hehe')
    pass

# os模块中没有复制文件的方法, 因为复制文件并非由操作系统提供的系统调用。

# shutil模块 是 os 模块的补充
# print([x for x in os.listdir('.') if os.path.isfile(x)])
# 将当前目录下的所有文件夹列出

# 要列出所有的.py文件，也只需一行代码：
# print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

# 小结
# Python的os模块封装了操作系统的目录和文件操作，要注意这些函数有的在os模块中，有的在os.path模块中。

from datetime import datetime
import os

pwd = os.path.abspath('.')

# print('      Size     Last Modified  Name')
# print('------------------------------------------------------------')
#
# for f in os.listdir(pwd):
#     fsize = os.path.getsize(f)
#     mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
#     flag = '/' if os.path.isdir(f) else ''
#     print('%10d  %s  %s%s' % (fsize, mtime, f, flag))

# 练习
#
# 利用os模块编写一个能实现dir -l输出的程序。
print(dir(-1))


# 2,编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
def findPath(url, regexs):
    allFiles = os.listdir(url)  # 获取所有的文件列表
    for files in allFiles:  # 遍历
        xPath = os.path.join(url, files)
        if os.path.isdir(files):  # 如果是文件夹
            findPath(xPath, regexs)
        elif os.path.isfile(xPath) and regexs in xPath:  # 如果是文件并且包含要查找的东西
            print(xPath)
