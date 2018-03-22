#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 注释 '

__author__ = 'zzh'

#
# struct
#
# Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换。

# print(b'\xe5\x91\xb5\xe5\x91\xb5')
import struct

# struct的pack函数把任意数据类型变成bytes：
b = struct.pack('>I', 10240099)
print(b)

# pack的第一个参数是处理指令，'>I'的意思是：
# >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
# 后面的参数个数要和处理指令一致。
#
# unpack把bytes变成相应的数据类型：
s = struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
print(s)

# 根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数。

s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00' \
    b'\x00\x68\x01\x00\x00\x01\x00\x18\x00'

s = struct.unpack('<ccIIIIIIHH', s)
print(type(s))

# 练习

# 请编写一个bmpinfo.py，可以检查任意文件是否是位图文件，如果是，打印出图片大小和颜色数。
import base64, struct

bmp_data = base64.b64decode('Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAAAAAAAAAAAAA'
                            '/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3/'
                            '/f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/AHwAfAB8AHz/f/9//3//f/9'
                            '//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//'
                            'f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9//3//f/9/AHwAfP9//3//f/9//3//f/9//3'
                            '8AfAB8AHwAfAB8AHwAfP9//3//f/9/AHwAfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AH'
                            'wAfAB8AHwAfAB8/3//f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3/'
                            '/f/9/AHwAfP9//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAfA'
                            'B8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9'
                            '/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//'
                            '3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')


def bmp_info(data):
    data = data[:30]
    result = struct.unpack('<ccIIIIIIHH', data)
    if result[0] == b'B' and result[1] == b'M':
        return {
            'width': result[6],
            'height': result[7],
            'color': result[9]
        }
    else:
        return {
            'width': 0,
            'height': 0,
            'color': 0
        }


# 测试
bi = bmp_info(bmp_data)
assert bi['width'] == 28
assert bi['height'] == 10
assert bi['color'] == 16
print('ok')
