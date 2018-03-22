#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 注释 '

__author__ = 'zzh'

#
# hmac
#
# Python自带的hmac模块实现了标准的Hmac算法。
# 而且 Hmac算法也支持 分块
#
# 我们首先需要准备待计算的原始消息message，随机key，哈希算法，这里采用MD5，使用hmac的代码如下：
# 创建默认为 MD5的方式 ,创建中 的 key 与 message 均为 byte 值
import hmac

message = b'Hello, world!'
key = b'score'
h = hmac.new(key, msg=message)  # 可以这样直接创建, 也可以先 new() 然后调用update
print(h.hexdigest())

h = hmac.new(key)
h.update(b'Hello,')
h.update(b' ')
h.update(b'world')
h.update(b'!')

print(h.hexdigest())

# 小结
#
# Python内置的hmac模块实现了标准的Hmac算法，它利用一个key对message计算“杂凑”后的hash，
# 使用hmac算法比标准hash算法更安全，因为针对相同的message，不同的key会产生不同的hash。

# 练习
import hmac, random


def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()


class User(object):
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = hmac_md5(self.key, password)


db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}


def login(username, password):
    user = db[username]
    return user.password == hmac_md5(user.key, password)


# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')
