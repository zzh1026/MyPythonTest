#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 注释 '

__author__ = 'zzh'

#
# 使用SQLite
#
# Python就内置了SQLite3，所以，在Python中使用SQLite，不需要安装任何东西，直接使用。
#
# 表是数据库中存放关系数据的集合，一个数据库里面通常都包含多个表，比如学生的表，班级的表，学校的表，等等。表和表之间通过外键关联。
# 要操作关系数据库，首先需要连接到数据库，一个数据库连接称为Connection
# 连接到数据库后，需要打开游标，称之为Cursor，通过Cursor执行SQL语句，然后，获得执行结果。

# 导入SQLite驱动:
import sqlite3

# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
conn = sqlite3.connect('zzh.db')

# 创建一个Cursor:
cursor = conn.cursor()

# 执行一条SQL语句，创建user表:
try:
    create_table_sql = 'create table user(id varchar(20) primary key,name varchar(20))'
    result = cursor.execute(create_table_sql)
except BaseException as e:
    print('exception: ', e.args)

# 继续执行一条SQL语句，插入一条记录
try:
    insert_user_sql = 'insert into user(id,name) values (\'1\',\'Michael\')'
    cursor.execute(insert_user_sql)
except BaseException as e:
    print('exception: ', e.args)

# 通过rowcount获得插入的行数:
rowcount = cursor.rowcount
print(rowcount)

# 关闭Cursor:
cursor.close()

# 提交事务:
conn.commit()

# 关闭Connection:
conn.close()

#
# 查询记录
#
conn = sqlite3.connect('zzh.db')
cursor = conn.cursor()

# 执行查询语句:
select_user_sql = 'select * from user where id=?'
cursor.execute(select_user_sql, ('1',))

# 获得查询结果集:
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()

# 使用Cursor对象执行insert，update，delete语句时，执行结果由rowcount返回影响的行数，就可以拿到执行结果。
# 使用Cursor对象执行select语句时，通过featchall()可以拿到结果集。结果集是一个list，每个元素都是一个tuple，对应一行记录。
# 如果SQL语句带有参数，那么需要把参数按照位置传递给execute()方法，有几个?占位符就必须对应几个参数，例如：
# cursor.execute('select * from user where name=? and pwd=?', ('abc', 'password'))

# 小结
#
# 在Python中操作数据库时，要先导入数据库对应的驱动，然后，通过Connection对象和Cursor对象操作数据。
# 要确保打开的Connection对象和Cursor对象都正确地被关闭，否则，资源就会泄露。


# 练习
#
# 请编写函数，在Sqlite中根据分数段查找指定的名字：
import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('CREATE TABLE user(id VARCHAR(20) PRIMARY KEY, name VARCHAR(20), score INT)')
cursor.execute(r"INSERT INTO user VALUES ('A-001', 'Adam', 95)")
cursor.execute(r"INSERT INTO user VALUES ('A-002', 'Bart', 62)")
cursor.execute(r"INSERT INTO user VALUES ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()


# ' 返回指定分数区间的名字，按分数从低到高排序 '
def get_score_in(low, high):
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute(r"SELECT name FROM user WHERE score BETWEEN ? AND ? ORDER BY score ASC", (low, high))
        result = [x[0] for x in cursor.fetchall()]
    finally:
        cursor.close()
        conn.commit()
        conn.close()
        return result


# 测试:
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('Pass')
