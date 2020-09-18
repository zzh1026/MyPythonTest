#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；

# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，
# 否则，你在源代码中写的中文输出可能会有乱码。

age = int(input('birth: '))


if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
