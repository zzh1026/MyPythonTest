#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 注释 '

__author__ = 'zzh'

#
# UDP编程
#
import socket

#
# 服务器
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # SOCK_DGRAM指定了这个Socket的类型是UDP
s.bind(('127.0.0.1', 9999))  # 绑定端口
print('Bind UDP on 9999...')
while True:
    # recvfrom()方法返回数据和客户端的地址与端口，这样，服务器收到数据后，直接调用sendto()就可以把数据用UDP发给客户端。
    data, addr = s.recvfrom(1024)  # 接收数据
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello, %s!' % data, addr)  # 正常的这里也应该是创建子线程的,否则就只能一个一个的响应

# 客户端使用UDP时，首先仍然创建基于UDP的Socket，然后，不需要调用connect()，直接通过sendto()给服务器发数据
#
# 客户端
# so = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# for data in [b'Michael', b'Tracy', b'Sarah']:
#     # 发送数据
#     so.sendto(data, ('127.0.0.1', 9999))
#     # 接收数据:
#     print(s.recv(1024).decode('utf-8'))
#
# so.close()

# 从服务器接收数据仍然调用recv()方法。

# DP的使用与TCP类似，但是不需要建立连接。此外，服务器绑定UDP端口和TCP端口互不冲突，也就是说，UDP的9999端口与TCP的9999端口可以各自绑定。
