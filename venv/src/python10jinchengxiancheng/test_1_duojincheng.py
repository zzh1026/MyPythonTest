#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 注释 '

__author__ = 'zzh'

import logging

logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.WARNING)
# logging.basicConfig(level=logging.ERROR)

#
# 多进程
#
#   multiprocessing中的Process类来代表一个进程对象,来创建一个进程
#   multiprocessing中的Pool类来代表一个进程池对象,来创建一个进程池
#   subprocess模块可以启动一个子进程，然后控制其输入和输出。
#   multiprocessing中的Queue、Pipes来进行进程间通信
#
#
# Python的os模块封装了常见的系统调用，其中就包括fork，可以在Python程序中轻松创建子进程：

import os

# logging.info('Progress (%s) start...' % (os.getppid()))

# Only works on Unix/Linux/Mac:
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

# Windows没有fork调用
# 有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务.
# 常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，就fork出子进程来处理新的http请求。

# multiprocessing(进程创建)
#
# Windows没有fork调用 , multiprocessing模块就是跨平台版本的多进程模块。
# multiprocessing模块提供了一个Process类来代表一个进程对象
# 下面的例子演示了启动一个子进程并等待其结束：
from multiprocessing import Process


# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)' % (name, os.getppid()))
    pass


# if __name__ == '__main__':
#     print('Parent process %s.' % os.getppid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')

# 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。
# join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。

#
# Pool(进程池)
# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
from multiprocessing import Pool
import os, time, random


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getppid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))
    pass


# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     # p = Pool()
#     for i in range(6):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')

# 代码解读：
# 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
# 请注意输出的结果，task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行，这是因为Pool的线程数量参数为4，这个参数可以不填,
# Pool 的默认线程数量为电脑CPU的数量
# 因此，最多同时执行4个进程。这是Pool有意设计的限制，并不是操作系统的限制。
#
# 由于Pool的默认大小是CPU的核数，如果你不幸拥有8核CPU，你要提交至少9个子进程才能看到上面的等待效果。
#

#
# 子进程
# subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
import subprocess

# print('$ nslookup www.google.com')
# r = subprocess.call(['nslookup', 'www.google.com'])
# print('exit code:', r)

#
# 进程间通信
# Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。
# 我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：
from multiprocessing import Process, Queue
import os, time, random


# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getppid())
    while True:
        value = q.get(True)
        print('Get %s from queue...' % value)


if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()

# 小结
#
# 在Unix/Linux下，可以使用fork()调用实现多进程。
# 要实现跨平台的多进程，可以使用multiprocessing模块。
# 进程间通信是通过Queue、Pipes等实现的。
