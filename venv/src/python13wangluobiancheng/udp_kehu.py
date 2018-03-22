#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 注释 '

__author__ = 'zzh'

import socket

# 客户端
so = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据
    so.sendto(data, ('127.0.0.1', 9999))
    # 接收数据:
    # print(so.recv(1024).decode('utf-8'))

so.close()
