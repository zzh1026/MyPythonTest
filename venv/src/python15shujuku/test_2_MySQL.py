#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 注释 '

__author__ = 'zzh'

#
# 使用MySQL
#
# MySQL是为服务器端设计的数据库，能承受高并发访问，同时占用的内存也远远大于SQLite。

# 导入MySQL驱动:
import mysql.connector

# 设置口令
conn = mysql.connector.connect(user='root', password='wszzh19921026', database='zzh')

# cursor = conn.cursor()
#
# # 创建user表:
# cursor.execute('CREATE TABLE user (id VARCHAR (20) PRIMARY KEY, name VARCHAR (20))')
#
# # 插入一行记录，注意MySQL的占位符是%s:
# cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
# cursor.rowcount
#
# # 提交事务:
# conn.commit()
# cursor.close()

# 运行查询:
# cursor = conn.cursor()
# cursor.execute('select * from user where id = %s', ('1',))
# values = cursor.fetchall()
# print(values)
# # 关闭Cursor和Connection:
# cursor.close()
# conn.close()
