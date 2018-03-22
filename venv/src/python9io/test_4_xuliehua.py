#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 注释 '

__author__ = 'zzh'

#
# 序列化
#
d = dict(name='bob', age=19, score=80)
di = {'name': 'bob', 'age': 18, 'score': 87}
# print(d)
# print(di)

# 变量从内存中变成可存储或传输的过程称之为序列化，
# 在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。

# 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
# 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
# Python提供了pickle模块来实现序列化。
import pickle

d = dict(name='bob', age=19, score=80)
b = pickle.dumps(d)
# print(b)

# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
# 或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
with open('dicts.txt', 'wb') as f:
    pickle.dump(d, f)

# 当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，
# 也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。
with open('dicts.txt', 'rb') as f:
    d = pickle.load(f)
    # print(d)
    pass

# Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python彼此都不兼容，
# 因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。


#
# JSON
#
# Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。我们先看看如何把Python对象变成一个JSON：
import json

d = dict(name='小明', age=99, score=80)
js = json.dumps(d)
# print(js)
# print(d)

# dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。
with open('json.txt', 'w') as f:
    json.dump(d, f)

# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
jsons = json.loads(json_str)
# print(jsons)

with open('json.txt', 'r') as f:
    bob = json.load(f)
    # print(bob)
    # f.seek(0)
    # print(f.readline())
    pass

#
# JSON进阶
#
# Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，我们更喜欢用class表示对象，比如定义Student类，然后序列化：
import json


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return 'name=%s,age=%s,score=%s' % (self.name, self.age, self.score)


s = Student('Bob', 20, 88)
# print(json.dumps(s, default=lambda obj: obj.__dict__))


# 因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。
#
# 同样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，
# 然后，我们传入的object_hook函数负责把dict转换为Student实例：
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


json_str = '{"age": 20, "score": 88, "name": "Bob"}'
# print(json.loads(json_str, object_hook=dict2student))
# print(json.loads(std_data, object_hook=lambda d: Student(d['name'], d['age'], d['score'])))

# 打印出的是反序列化的Student实例对象。

# 练习
# 对中文进行JSON序列化时，json.dumps()提供了一个ensure_ascii参数，观察该参数对结果的影响：
obj = dict(name='小明', age=20)
s = json.dumps(obj)
print(s)
s = json.dumps(obj, ensure_ascii=True)
print(s)
s = json.dumps(obj, ensure_ascii=False)
print(s)

# 小结
# Python语言特定的序列化模块是pickle，但如果要把序列化搞得更通用、更符合Web标准，就可以使用json模块.
#
# json模块的dumps()和loads()函数是定义得非常好的接口的典范。当我们使用时，只需要传入一个必须的参数。
# 但是，当默认的序列化或反序列机制不满足我们的要求时，我们又可以传入更多的参数来定制序列化或反序列化的规则，
# 既做到了接口简单易用，又做到了充分的扩展性和灵活性。
#
# json 和 pickle 模块分别
#   提供了 dump 和dumps 方法用来进行序列化 ,这两个方法的区别是 dump 需要like - file object 参数来将序列化以后
#       的内容直接写入 , 而 dumps 主要是生成 序列化以后的内容, 并不会存储在磁盘上, 存储于内存中
#   同时还提供了 load 和loads 方法用来进行反序列化 , 这两个方法的区别是 load 需要 like - file object 参数来直接从磁盘文件
#       的内容反序列化出来, 而 loads 主要是在内存中进行反序列化, 即loads 的参数主要为 一个str

