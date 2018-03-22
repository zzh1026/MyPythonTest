#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 注释 '

__author__ = 'zzh'

#
# 使用SQLAlchemy
#
# ORM技术：Object-Relational Mapping，把关系数据库的表结构映射到对象上。
# 在Python中，最有名的ORM框架是SQLAlchemy。
#
# 安装:  pip install sqlalchemy

# 1, 导入SQLAlchemy，并初始化DBSession
from sqlalchemy import Column, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 2, 创建对象的基类:
Base = declarative_base()


# 3, 定义User对象
class User(Base):
    # 表的名字
    __tablename__ = 'user'

    # 表的结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


# 4, 初始化数据库链接
engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
print(engine)

# 5, 创建DBSession类型
DBSession = sessionmaker(bind=engine)
print(DBSession)

# 以上代码完成SQLAlchemy的初始化和具体每个表的class定义。如果有多个表，就继续定义其他class，例如School：
# create_engine()用来初始化数据库连接, SQLAlchemy用一个字符串表示连接信息：
# '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'

# 向数据库表中添加一行记录，可以视为添加一个User对象：

# 创建session对象
session = DBSession()
# 创建新User对象
new_user = User(id='5', name='Bob')
# 添加到session
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()

# 有了ORM，查询出来的可以不再是tuple，而是User对象。
# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id == '5').one()
# 打印类型和对象的name属性:
print('type:', type(user))
print('name:', user.name)
# 关闭Session:
session.close()


# ORM就是把数据库表的行与相应的对象建立关联，互相转换。
# 由于关系数据库的多个表还可以用外键实现一对多、多对多等关联，相应地，ORM框架也可以提供两个对象之间的一对多、多对多等功能。
# 例如，如果一个User拥有多个Book，就可以定义一对多关系如下：
class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # 一对多:
    books = relationship('Book')


class Book(Base):
    __tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # “多”的一方的book表是通过外键关联到user表的:
    user_id = Column(String(20), ForeignKey('user.id'))

# 小结
#
# ORM框架的作用就是把数据库表的一行记录与一个对象互相做自动转换。
#
# 正确使用ORM的前是了解关系数据库的原理。
