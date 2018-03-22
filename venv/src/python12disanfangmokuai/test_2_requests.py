#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 注释 '

__author__ = 'zzh'

#
# requests
#
# Python内置的urllib模块来访问网络资源用起来比较麻烦，而且，缺少很多实用的高级功能。
# 一般使用 requests。它是一个Python第三方库，处理URL资源特别方便。
#
# 安装
# $ pip install requests

# 使用requests
# GET访问
import requests

# r = requests.get('https://www.douban.com/')
# print(r.status_code)

# 1, url添加参数
#
# 对于带参数的URL，传入一个dict作为params参数
params = {'q': 'python', 'cat': '1001'}

# 2, url添加header
#
# 传入一个dict作为headers参数
headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'}

# 3, 添加 cookie
#
# 准备一个dict传入cookies参数
cookies = {'token': '12345', 'status': 'working'}

# 4, 添加超时时间 , 传入以秒为单位的 timeout参数
timeout = 3

r = requests.get('https://www.douban.com/search', params=params, headers=headers, cookies=cookies, timeout=timeout)
print(r.text)

# 无论响应是文本还是二进制内容，我们都可以用content属性获得bytes对象, 也可以通过text获取内容对象
# print(r.content)
# print(r.text)
# print(r.url)  # 实际请求的URL
# print(r.encoding)  # requests自动检测编码，可以使用encoding属性查看
# print(r.json())  # 对于特定类型的响应,可以直接获取
# print(r.headers)  # 获取响应头
# print(dict(r.cookies))  # 获取所有的cookie 可以转换成dict
# print(r.cookies.get('ts', None))  # 获取某个cookie(名称为 ts 的cookie)

#
# POST请求
#
# 把get()方法变成post()，然后传入data参数作为POST请求的数据
# r = requests.post('https://accounts.douban.com/login',
#                   data={'form_email': 'abc@example.com', 'form_password': '123456'})
# print(r.text)

# requests默认使用application/x-www-form-urlencoded对POST数据编码。如果要传递JSON数据，可以直接传入json参数

# 上传文件 ,requests把它简化成files参数
# upload_files = {'file': open('new.jgp', 'rb')}
# r = requests.post(url, files=upload_files)
