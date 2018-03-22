#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 注释 '

__author__ = 'zzh'

# 导入socket库:
import socket

# 客户端
import chardet


def create_socket():
    # 创建一个socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET指定使用IPv4协议 ,SOCK_STREAM指定使用面向流的TCP协议

    # 建立连接
    b = s.connect(('www.sina.com.cn', 80))  # 参数是一个tuple，包含地址和端口号

    # 发送数据
    sendData = b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n'
    s.send(sendData)

    # 接收数据
    buffer = []
    while True:
        d = s.recv(1024)  # 每次最多接收1k字节
        if d:
            buffer.append(d)
        else:
            break

    reData = b''.join(buffer)

    # 关闭连接
    s.close()

    header, html = reData.split(b'\r\n\r\n', 1)
    print(header.decode('utf-8'))
    # 把接收的数据写入文件:
    with open('sina.html', 'wb') as f:
        f.write(html)


# create_socket()

# ------------------------------------分割线------------------------------------------------------------
# 测试该 server.py服务器 的客户端
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 9999))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))
for data in [b'zzh', b'hehe', b'lala']:
    # 发送数据:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
