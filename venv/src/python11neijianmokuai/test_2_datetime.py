#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 注释 '

__author__ = 'zzh'

#
# datetime
#
# datetime是Python处理日期和时间的标准库。
#
from datetime import datetime

# datetime是模块，datetime模块还包含一个datetime类，通过from datetime import datetime导入的才是datetime这个类。
# 如果仅导入import datetime，则必须引用全名datetime.datetime。
# datetime.now()返回当前日期和时间，其类型是datetime。

# 1, 获取当前日期和时间
now = datetime.now()  # 获取当前datetime
# print(now)
now = datetime.utcnow()  # 获取当前datetime
# print(now)

# 2, 获取指定日期和时间
dt = datetime(2019, 3, 4, 23, 45, 56)  # 用指定日期时间创建datetime
# print(dt)

# 3 ,datetime转换为timestamp ,调用timestamp()方法
ts = dt.timestamp()  # 把datetime转换为timestamp
# print(ts)
# >>> 1551714356.0      小数点后为 毫秒数, 小数点前为 秒

# 4, timestamp转换为datetime ,使用datetime提供的fromtimestamp()方法
t = 1429417200.0
time = datetime.fromtimestamp(t)  # 当前时区时间
# print(time)
time2 = datetime.utcfromtimestamp(t)  # 标准时区时间:UTC时间
# print(time2)

# 5, str转换为datetime , 转换方法是通过datetime.strptime()实现，需要一个日期和时间的格式化字符串
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
# print(cday)
# 字符串'%Y-%m-%d %H:%M:%S'规定了日期和时间部分的格式。转换后的datetime是没有时区信息, 即为当前时区的时间

# 6, datetime转换为str , 通过strftime()实现，同样需要一个日期和时间的格式化字符串
# strs = now.strftime('%a, %b %d %H:%M')
strs = now.strftime('%Y-%m %d and %H:%M')
# print(strs)

# 7, datetime加减 ,日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。
#       加减可以直接用+和-运算符，不过需要导入timedelta这个类,增加或者减少的时间需要用 timedelta进行包装
from datetime import timedelta

now = datetime.now()
# print(now)
t1 = now + timedelta(hours=10)
# print(t1)
t2 = now - timedelta(days=1)
# print(t2)

# 8, 本地时间转换为UTC时间
# 本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间。
# 一个datetime类型有一个时区属性tzinfo，但是默认为None，所以无法区分这个datetime到底是哪个时区，除非强行给datetime设置一个时区：
from datetime import datetime, timedelta, timezone

tz_utc_8 = timezone(timedelta(hours=8))  # 创建时区UTC+8:00
now = datetime.now()
# print(now)

dts = datetime.utcnow()
# print(dts)

dt = now.replace(tzinfo=tz_utc_8)  # 强制设置为UTC+8:00
print(dt)

# 9, 时区转换 , 先通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间

# 拿到UTC时间，并强制设置时区为UTC+0:00:
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)

# astimezone()将转换时区为北京时间:
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)

# astimezone()将转换时区为东京时间:
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)

# astimezone()将bj_dt转换时区为东京时间:
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)
s = tokyo_dt2.timestamp()
print('s=', s, ' and now = ', now.timestamp())

# 时区转换的关键在于，拿到一个datetime时，要获知其正确的时区，然后强制设置时区，作为基准时间。
# 利用带时区的datetime，通过astimezone()方法，可以转换到任意时区。
# 不是必须从UTC+0:00时区转换到其他时区，任何带时区的datetime都可以正确转换，例如上述bj_dt到tokyo_dt的转换。


# 小结
# datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。
# 如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。是独立的

# 练习
# 假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp：
import re
from datetime import datetime, timezone, timedelta


def to_timestamp(dt_str, tz_str):
    # regex = r'+(\d+):'
    # hours = re.match(regex, tz_str).group(1)
    # cday = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    # t1 = cday + timedelta(hours=hours)
    # return t1.timestamp()

    tz = re.match(r'UTC([+-]\d+):\d+', tz_str).group(1)
    time = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    realtime = time.replace(tzinfo=timezone(timedelta(hours=int(tz))))
    print('realtime\'s type is', type(realtime))
    return realtime.timestamp()


# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')
