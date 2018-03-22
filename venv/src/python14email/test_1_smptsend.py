#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 注释 '

__author__ = 'zzh'

#
# SMTP发送邮件
#
# SMTP是发送邮件的协议
# 有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。
from email.mime.text import MIMEText

# 创建邮件
# 第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'表示纯文本，最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性
msg = MIMEText('hello world zzh', 'plain', 'utf-8')

# 输入Email地址和口令
from_addr = input('From: ')
password = input('password: ')

# 输入收件人地址
to_addr = input('To: ')
# 输入SMTP服务器地址
smtp_server = input('SMTP server')

# 发送邮件
import smtplib

server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
server.set_debuglevel(1)  # set_debuglevel(1)可以打印出和SMTP服务器交互的所有信息
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()
