#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# create by zzh


# 模块
#
# 在Python中，一个.py文件就称之为一个模块（Module）。
#
#
# 模块是一组Python代码的集合，可以使用其他模块，也可以被其他模块使用。
#
#
# 创建自己的模块时，要注意：
#
#   1 , 模块名要遵循Python变量命名规范，不要使用中文、特殊字符；
#   2 , 模块名不要和系统模块名冲突，最好先查看系统是否已存在该模块，检查方法是在Python交互环境执行import abc，若成功则说明系统存在此模块。

# import src.python4hanshushibiancheng.test_6_niminghanshu

# import src.python5mokuai.test_1_usemokuai as lll      #这是从最外层导入的方法

# print(lll.greeting('啦啦啦啦'))


# 导入规则
#
# import xxx 是从 Python 系统库，或者项目的最外层导入 xxx。)
# from . import xxx 是从同一文件夹下导入 xxx。 (当前文件夹导入其他模块)
# from .yyy import xxx 是从当前目录的子文件夹 yyy 中导入 xxx。(当前目录的子文件夹)
#
# 如果要导入上层目录的模块则需要使用外层导入的方法


