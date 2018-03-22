#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 注释 '

__author__ = 'zzh'

if __name__ == '__main__':
    pass

#
# 在Python中，安装第三方模块，是通过包管理工具pip完成的。
#
# 一般来说，第三方库都会在Python官方的pypi.python.org网站注册，要安装一个第三方库，必须先知道该库的名称，
# 可以在官网或者pypi上搜索，比如Pillow的名称叫Pillow，因此，安装Pillow的命令就是：
#
# pip install Pillow
#

# 安装常用模块
# https://www.anaconda.com/download

# 模块搜索路径
#
# 当我们试图加载一个模块时，Python会在指定的路径下搜索对应的.py文件，如果找不到，就会报错：
#
# 默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中：

# import sys
#
# print(sys.path)
