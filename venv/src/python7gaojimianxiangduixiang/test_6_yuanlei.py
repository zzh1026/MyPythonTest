#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 注释 '

__author__ = 'zzh'


# 使用元类
#
#
# 1 , type()
#       type()函数可以查看一个类型或变量的类型
#
# python是动态语言, 其class的定义是运行时动态创建的，而创建class的方法就是使用type()函数。
#
# type()函数既可以返回一个对象的类型，又可以创建出新的类型，
# 比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义：
def fn(self, name='world'):  # 先定义函数
    print('Hello, %s.' % name)


Hello = type('Hello', (object,), dict(hello=fn))  # 创建Hello class
h = Hello()


# h.hello()

# print(type(Hello))
# print(type(h))


# 要创建一个class对象，type()函数依次传入3个参数：
# 1, class的名称；
# 2, 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；(object,) 这是一个tuple而非一个对象
# 3, class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
#
# 通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，
#   然后调用type()函数创建出class。

# 正常情况下，我们都用class Xxx...来定义类，但是，type()函数也允许我们动态创建出类来，
# 也就是说，动态语言本身支持运行期动态创建类，这和静态语言有非常大的不同，
# 要在静态语言运行期创建类，必须构造源代码字符串再调用编译器，或者借助一些工具生成字节码实现，本质上都是动态编译，会非常复杂。


# metaclass
#
# 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。
# metaclass，直译为元类，简单的解释就是：
# 当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。 这个过程: 定义类 -> 创建实例
# 但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。 这个过程: 定义metaclass ->创建类
# 连接起来就是：先定义metaclass，就可以创建类，最后创建实例。 这个过程:定义metaclass -> 创建类 -> 创建实例
#
# 所以，metaclass允许创建类或者修改类。换句话说，可以把类看成是metaclass创建出来的“实例”。

# 使用metaclass给我们自定义的MyList增加一个add方法：
#
# 1 , 定义ListMetaclass，按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass：
class ListMetaclass(type):  # metaclass是类的模板，所以必须从`type`类型派生：
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, values: self.append(values)
        return type.__new__(cls, name, bases, attrs)


# 有了ListMetaclass，我们在定义类的时候还要指示使用ListMetaclass来定制类，传入关键字参数metaclass：
class MyList(list, metaclass=ListMetaclass):  # 这个Mylist上本质上有两个参数, 第一个是继承自list类, 第二个指定了metaclass
    pass


# 当我们传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时，
# 要通过ListMetaclass.__new__()来创建，在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。
#
# __new__()方法接收到的参数依次是：
# cls , 当前准备创建的类的对象；
# name , 类的名字；
# bases , 类继承的父类集合；
# attrs , 类的方法集合。

# 测试一下MyList是否可以调用add()方法： 普通的list是没有add()方法的,继承自list 的MyList添加了 add方法
L = MyList()
L.add('lim')


# print(L)


#
# 动态修改类一般用不到,但是ORM就是需要通过metaclass修改类定义的
#
# 要编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。
#
# 编写底层模块的第一步，就是先把调用接口写出来。
# 比如，使用者如果使用这个ORM框架，想定义一个User类来操作对应的数据库表User，我们期待他写出这样的代码：

# class User(Modle):  # 这个Usermodle继承自Modle
#     # 定义类的属性到列的映射：
#     id = IntegerField('id')
#     name = StringField('username')
#     email = StringField('email')
#     password = StringField('password')
#
#
# # 创建一个实例：
# u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# # 保存到数据库：
# u.save()


#
# 其中，父类Model和属性类型StringField、IntegerField是由ORM框架提供的，剩下的魔术方法比如save()全部由metaclass自动完成。
# 虽然metaclass的编写会比较复杂，但ORM的使用者用起来却异常简单。
#
# 首先来定义Field类，它负责保存数据库表的字段名和字段类型：
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


# 在Field的基础上，进一步定义各种类型的Field，比如StringField，IntegerField等等：
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


# 下一步，就是编写最复杂的ModelMetaclass了：
class ModleMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Modle':  # 排除掉对Model类的修改
            return type.__new__(cls, name, bases, attrs)
        print('Fond Modle: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping : %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)


# 创建基类Model：
class Modle(dict, metaclass=ModleMetaclass):
    def __init__(self, **kw):
        super(Modle, self).__init__(**kw)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


# 当用户定义一个class User(Model)时，Python解释器首先在当前类User的定义中查找metaclass，
# 如果没有找到，就继续在父类Model中查找metaclass，找到了，就使用Model中定义的metaclass的ModelMetaclass来创建User类，
# 也就是说，metaclass可以隐式地继承到子类，但子类自己却感觉不到。

# 在ModelMetaclass中，一共做了几件事情：
# 1,排除掉对Model类的修改；
# 2,在当前类（比如User）中查找定义的类的所有属性，如果找到一个Field属性，就把它保存到一个__mappings__的dict中，同时从类属性中删除该Field属性，
#   否则，容易造成运行时错误（实例的属性会遮盖类的同名属性）；
# 3,把表名保存到__table__中，这里简化为表名默认为类名。

# 在Model类中，就可以定义各种操作数据库的方法，比如save()，delete()，find()，update等等。
class User(Modle):  # 这个Usermodle继承自Modle
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()
