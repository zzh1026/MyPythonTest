#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 注释 '

__author__ = 'zzh'

#
# 分布式进程
# 在Thread和Process中，应当优选Process，因为Process更稳定，而且，Process可以分布到多台机器上，
# 而Thread最多只能分布到同一台机器的多个CPU上。

# Python的multiprocessing模块不但支持多进程，其中managers子模块还支持把多进程分布到多台机器上。
# 一个服务进程可以作为调度者，将任务分布到其他多个进程中，依靠网络通信。
# 由于managers模块封装很好，不必了解网络通信的细节，就可以很容易地编写分布式多进程程序。
#
# 如果我们已经有一个通过Queue通信的多进程程序在同一台机器上运行，
# 现在，由于处理任务的进程任务繁重，希望把发送任务的进程和处理任务的进程分布到两台机器上。怎么用分布式进程实现？
# 原有的Queue可以继续使用，但是，通过managers模块把Queue通过网络暴露出去，就可以让其他机器的进程访问Queue了。
#
# 我们先看服务进程，服务进程负责启动Queue，把Queue注册到网络上，然后往Queue里面写入任务：
#
# task_master.py
#
# 然后，在另一台机器上启动任务进程（本机上启动也可以）：
#
# task_worker.py
#
#
# Queue对象存储在哪？注意到task_worker.py中根本没有创建Queue的代码，所以，Queue对象存储在task_master.py进程中：
# 而Queue之所以能通过网络访问，就是通过QueueManager实现的。
# 由于QueueManager管理的不止一个Queue，所以，要给每个Queue的网络调用接口起个名字，比如get_task_queue。

#
# 小结
#
# Python的分布式进程接口简单，封装良好，适合需要把繁重任务分布到多台机器的环境下。
# 注意Queue的作用是用来传递任务和接收结果，每个任务的描述数据量要尽量小。比如发送一个处理日志文件的任务，就不要发送几百兆的日志文件本身，
# 而是发送日志文件存放的完整路径，由Worker进程再去共享的磁盘上读取文件。
