#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 注释 '

__author__ = 'zzh'

#
# chardet
#
# 用来检测编码，简单易用。 对于对未知编码的bytes 转换成str
#
# 安装chardet
#
# $ pip install chardet

# 使用chardet
#
# 当我们拿到一个bytes时，就可以对其检测编码。用chardet检测编码, 使用detect() 方法
import chardet

data = b'Hello, world!'
cd = chardet.detect(data)  # 返回一个dict
print(cd)
result = data.decode(cd.get('encoding', 'utf-8'))
print('result=', result)

# 检测出的编码是ascii，注意到还有个confidence字段，表示检测的概率是1.0（即100%）。

data = '离离原上草，一岁一枯荣'.encode('gbk')
cd = chardet.detect(data)
print(cd)
result = data.decode(cd.get('encoding', 'utf-8'))
print('result=', result)

data = '离离原上草，一岁一枯荣'.encode('utf-8')
cd = chardet.detect(data)
print(cd)
result = data.decode(cd.get('encoding', 'utf-8'))
print('result=', result)

data = '最新の主要ニュース'.encode('euc-jp')
cd = chardet.detect(data)
print(cd)
result = data.decode(cd.get('encoding', 'utf-8'))
print('result=', result)
