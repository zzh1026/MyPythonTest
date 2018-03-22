#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 注释 '

__author__ = 'zzh'

#
# 常用第三方模块
#
# 基本上，所有的第三方模块都会在PyPI - the Python Package Index上注册，只要找到对应的模块名字，即可用pip安装。
#
# 1, Pillow ,图片处理器 , 主要流程 Image.open() 打开, im.rotate() 操作, im.save('','') 保存
# 2, requests, 网络框架, 主要流程, requests.get/post,默认可传 params ,可选参数有headers, cookie, timeout等配置参数,还能上传文件
# 3, chardet, 对一个 bytes 通过 chardet.detect(data) 的方式检测其编码方式
# 4, psutil, 系统信息获取框架
#
