#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 注释 '

__author__ = 'zzh'

# 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径

import os


# print(os.listdir('.'))


def findPath(url, regexs):
    allFiles = os.listdir(url)  # 获取所有的文件列表
    for files in allFiles:  # 遍历
        xPath = os.path.join(url, files)
        if os.path.isdir(files):  # 如果是文件夹
            findPath(xPath, regexs)
        elif os.path.isfile(xPath) and regexs in xPath:  # 如果是文件并且包含要查找的东西
            print(xPath)


findPath('.', 'test')
