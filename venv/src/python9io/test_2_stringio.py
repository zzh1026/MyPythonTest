#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 注释 '

__author__ = 'zzh'

#
# StringIO和BytesIO
#
#   StringIo和BytesIO使用read 方法是通过指针的方式来进行的
#
# StringIO

#
# StringIO顾名思义就是在内存中读写str。
# 要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可：
from io import StringIO

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print(f.getvalue())  # f是写出的,可以通过getvalue 的方法 获取写出的内容
f.seek(0)
print(f.read())  # f是写出的,所以当前的指针在最后一个字符上,其read方法值为空,需要将指针跳转到0 read 方法才能重新读取到

# getvalue()方法用于获得写入后的str。

# 要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：
f = StringIO('Hello!\nHi!\nGoodbye!')
print(f.readline().strip())
print('->')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

# BytesIO
#
# StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
# BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes：
from io import BytesIO

f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())  # f为写出, 可以通过getvalue来获取内容,但是此时指针在最后一个字符后,read 方法则为空,需要通过seek方法调整指针

# read from BytesIO:
data = '人闲桂花落，夜静春山空。月出惊山鸟，时鸣春涧中。'.encode('utf-8')
f = BytesIO(data)
print(f.read())  # f为一个对象,相当于写入,可以通过 read方法来读, 但是事二进制的

# 小结
# StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。

# StringIO和BytesIO

# stringIO 比如说，这时候，你需要对获取到的数据进行操作，但是你并不想把数据写到本地硬盘上，这时候你就可以用stringIO
from io import StringIO
from io import BytesIO


def outputstring():
    return 'string \nfrom \noutputstring \nfunction'


s = outputstring()

# 将函数返回的数据在内存中读
sio = StringIO(s)
# 可以用StringIO本身的方法
print(sio.getvalue())
# 也可以用file-like object的方法
s = sio.readlines()
for i in s:
    print(i.strip())

# 将函数返回的数据在内存中写
sio = StringIO()
# sio.write(s)
# 可以用StringIO本身的方法查看
s = sio.getvalue()
print(s)

# 如果你用file-like object的方法查看的时候，你会发现数据为空
sio = StringIO()
sio.write(s)
for i in sio.readlines():
    print(i.strip())

# 这时候我们需要修改下文件的指针位置
# 我们发现可以打印出内容了
sio = StringIO()
sio.write(s)
sio.seek(0, 0)
print(sio.tell())
for i in sio.readlines():
    print(i.strip())

# 这就涉及到了两个方法seek 和 tell
# tell 方法获取当前文件读取指针的位置
# seek 方法，用于移动文件读写指针到指定位置,有两个参数，第一个offset: 偏移量，需要向前或向后的字节数，正为向后，负为向前；
#       第二个whence: 可选值，默认为0，表示文件开头，1表示相对于当前的位置，2表示文件末尾
# 用seek方法时，需注意，如果你打开的文件没有用'b'的方式打开，则offset无法使用负值哦


# stringIO 只能操作str，如果要操作二进制数据，就需要用到BytesIO
# 上面的sio无法用seek从当前位置向前移动，这时候，我们用'b'的方式写入数据，就可以向前移动了
bio = BytesIO()
bio.write(s.encode('utf-8'))
print(bio.getvalue())
bio.seek(-36, 1)
print(bio.tell())
for i in bio.readlines():
    print(i.strip())
