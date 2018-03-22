#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 注释 '

__author__ = 'zzh'

#
# base64
#
# Base64是一种用64个字符来表示任意二进制数据的方法。
#
# Python内置的base64可以直接进行base64的编解码：
import base64

b = base64.b64encode(b'binary\x00string')
print(b)

b = base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
print(b)

b = base64.b64encode('服了服了'.encode())
print(b)

b = base64.b64decode('5pyN5LqG5pyN5LqG')
print(b)

# 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：
b = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(b)

b = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(b)

b = base64.urlsafe_b64decode('abcd--__')
print(b)


# Base64是一种通过查表的编码方法，不能用于加密，即使使用自定义的编码表也不行。
#
# Base64适用于小段内容的编码，比如数字证书签名、Cookie的内容等。
#
# 由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，所以，很多Base64编码后会把=去掉：
# 去掉=后怎么解码的时候, 因为Base64是把3个字节变为4个字节，所以，Base64编码的长度永远是4的倍数，
# 因此，需要加上=把Base64字符串的长度变为4的倍数，就可以正常解码了。

#
# 小结
#
# Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。


# 练习
# 请写一个能处理去掉=的base64解码函数
def safe_base64_decode(s):
    # num = len(s) % 4
    # result = b''
    # while 4 - num > 0:
    #     result += b'='
    #     num += 1
    # s += result
    # return base64.b64decode(s)
    s = s + (4 - len(s) % 4) % 4 * b'='
    return base64.b64decode(s)


# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')

s = base64.b64encode('在Python中使用BASE 64编码'.encode('utf-8'))
print(s)
d = base64.b64decode(s).decode('utf-8')
print(d)

s = base64.urlsafe_b64encode('在Python中使用BASE 64编码'.encode('utf-8'))
print(s)
d = base64.urlsafe_b64decode(s).decode('utf-8')
print(d)
