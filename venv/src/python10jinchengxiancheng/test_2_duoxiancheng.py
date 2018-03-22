#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 注释 '

__author__ = 'zzh'

#
# 多线程
#
# 进程是由若干线程组成的，一个进程至少有一个线程。线程是操作系统直接支持的执行单元.
#
# Python的线程是真正的Posix Thread，而不是模拟出来的线程。
#
# Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。
# 绝大多数情况下，我们只需要使用threading这个高级模块。
#
# 启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行：
import threading
import time


# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='heheThread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)

# 任何进程默认就会启动一个线程，该线程称为主线程，主线程又可以启动新的线程，
# Python的threading模块有个current_thread()函数，它永远返回当前线程的实例。主线程实例的名字叫MainThread

#
# Lock
#
# 同步锁
# 创建一个锁就是通过threading.Lock()来实现

# lock = threading.Lock()  # 创建锁
# lock.acquire()  # 获取锁
# lock.release()  # 释放锁

import time, threading

# 假定这是你的银行存款:
balance = 0


def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(1000000):
        change_it(n)


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print('balance=', balance)


# 当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁，然后继续执行代码，其他线程就继续等待直到获得锁为止。
# 获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为死线程。所以我们用try...finally来确保锁一定会被释放。
def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()


#
# 多核CPU的Python死循环
import threading, multiprocessing, os


def loop():
    x = 0
    while True:
        x = x ^ 1


print(os.cpu_count())
print(multiprocessing.cpu_count())
for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    # t.start()

# 因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，
# 任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。
# 这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。

#
# ThreadLocal (ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题)
#
# 在多线程环境下，每个线程都有自己的数据。一个线程使用自己的局部变量比使用全局变量好，因为局部变量只有线程自己能看见，
# 不会影响其他线程，而全局变量的修改必须加锁。
#
# 但是局部变量也有问题，就是在函数调用的时候，其参数值需要传递.
import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()


def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()


t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

# 全局变量local_school就是一个ThreadLocal对象，每个Thread对它都可以读写student属性，但互不影响。
# 你可以把local_school看成全局变量，但每个属性如local_school.student都是线程的局部变量，可以任意读写而互不干扰，
# 也不用管理锁的问题，ThreadLocal内部会处理。
#
# 可以理解为全局变量local_school是一个dict，不但可以用local_school.student，还可以绑定其他变量，如local_school.teacher等等。
#
# ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，
# 这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。

# 小结
# 多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。
# Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦。
#
# 一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。
# ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。
