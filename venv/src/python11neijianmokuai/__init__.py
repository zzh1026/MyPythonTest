#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 注释 '

__author__ = 'zzh'

#
# 正则表达式 和 常用内建模块
#
# 正则表达式一般用来匹配整个字符串, 使用分组方法的时候匹配到的是符合条件的字符串
#
# Python之所以自称“batteries included”，就是因为内置了许多非常有用的模块，无需额外安装和配置，即可直接使用。
#
# 1, datetime, 处理日期和时间
# 2, collections ,集合工具类 ,包括 tuple ,list ,dict ,计数器counter
# 3, base64, 一种用64个字符来表示任意二进制数据的方法
# 4, struct, bytes和其他二进制数据类型的转换 , 通过 pack 和unpack 两个方法来进行转换和反向
# 5, hashlib, 摘要算法,主要是md5和sha1的算法处理,方式是:1, hashlib.md5() 创建. 2, md5.update() 处理, 3, md5.hexdigest()输出
# 6, hmac, 使程序算法更标准安全, 通过加盐的 md5 和 sha1 更加安全
# 7, itertools, 操作迭代对象, 创建无限迭代对象, 可以不用
# 8, contextlib , 主要通过 @contextmanager 和 @closing 等的 generator来简化上下文管理,可以不用
# 9, urllib, 用来发送 get或者 post 请求.
# 10,XML, xml 的解析 xml.parsers.expat 中的ParserCreate ,和 xml生成的字符串拼接
# 11,HTMLParser, Html的标签解析 ,主要使用 html.parser 中的 HTMLParser.
#
