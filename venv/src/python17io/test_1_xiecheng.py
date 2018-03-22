#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 注释 '

__author__ = 'zzh'


#
# 协程
#
# 协程执行，在执行A的过程中，可以随时中断，去执行B，B也可能在执行过程中中断再去执行A
#
# 协程的特点在于是一个线程执行
#
# 多线程比，协程的优势在于:
#   1, 执行效率极高, 因为子程序切换不是线程切换，而是由程序自身控制，因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显。
#   2, 不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突
#
#
# Python对协程的支持是通过generator实现的。
def consumer():
    r = ''
    while True:
        n = yield r
        print('n = ', n)
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


c = consumer()
produce(c)

#
# consumer函数是一个generator，把一个consumer传入produce后
# 1, 首先调用c.send(None)启动生成器；
# 2, 然后，一旦生产了东西，通过c.send(n)切换到consumer执行
# 3, consumer通过yield拿到消息，处理，又通过yield把结果传回
# 4, produce拿到consumer处理的结果，继续生产下一条消息
# 5, produce决定不生产了，通过c.close()关闭consumer，整个过程结束。
#
# 整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。
