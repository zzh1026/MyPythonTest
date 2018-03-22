#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 注释 '

__author__ = 'zzh'

#
# hashlib
#
# Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。
#
# 摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，目的是为了发现原始数据是否被人篡改过。

#
# 计算字符串的MD5值
import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

# 如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的：
md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

# 另一种常见的摘要算法是SHA1，调用SHA1和调用MD5完全类似：同时 sha1 也可以分块多次调用update()
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())


# 比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且摘要长度更长。

# 练习
# 根据用户输入的口令，计算出存储在数据库中的MD5口令：
def calc_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()


db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}


def login(user, password):
    inputMd5 = db.get(user, '')
    resultMd5 = calc_md5(password)
    return inputMd5 == resultMd5


# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

# 练习
# 根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5：
db = {}


def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')


# register('bob', '123546')
# print(db['bob'])

# 然后，根据修改后的MD5算法实现用户登录的验证：
import hashlib, random


class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)


db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}


def login(username, password):
    user = db[username]
    return user.password == get_md5(password)


# 测试:
# assert login('michael', '123456')
# assert login('bob', 'abc999')
# assert login('alice', 'alice2008')
# assert not login('michael', '1234567')
# assert not login('bob', '123456')
# assert not login('alice', 'Alice2008')
# print('ok')

# 摘要算法在很多地方都有广泛的应用。要注意摘要算法不是加密算法，不能用于加密（因为无法通过摘要反推明文），只能用于防篡改，
# 但是它的单向计算特性决定了可以在不存储明文口令的情况下验证用户口令。
