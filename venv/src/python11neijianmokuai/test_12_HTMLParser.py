#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 注释 '

__author__ = 'zzh'

from html.entities import name2codepoint
#
# HTMLParser
#
# 如果我们要编写一个搜索引擎，第一步是用爬虫把目标网站的页面抓下来，第二步就是解析该HTML页面，看看里面的内容到底是新闻、图片还是视频。
#
# Python提供了HTMLParser来非常方便地解析HTML，只需简单几行代码
#
from html.parser import HTMLParser


class MyHtmlParser(HTMLParser):
    def handle_starttag(self, tag, attrs):  # 标签开始
        print('handle_starttag: <%s>' % tag)

    def handle_endtag(self, tag):  # 标签结尾
        print('handle_endtag: </%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('handle_startendtag: <%s/>' % tag)

    def handle_data(self, data):  # 内容
        print('handle_data:', data)

    def handle_comment(self, data):  # 注释
        print('handle_comment: <!--', data, '-->')

    def handle_entityref(self, name):
        print('handle_entityref: &%s;' % name)

    def handle_charref(self, name):
        print('handle_charref: &#%s;' % name)


# parser = MyHtmlParser()
# parser.feed('''<html>
# <head></head>
# <body>
# <!-- test html parser -->
#     <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
# </body></html>''')

# feed()方法可以多次调用，也就是不一定一次把整个HTML字符串都塞进去，可以一部分一部分塞进去。
#
# 特殊字符有两种，一种是英文表示的&nbsp;，一种是数字表示的&#1234;，这两种字符都可以通过Parser解析出来。

# 小结
#
# 利用HTMLParser，可以把网页中的文本、图像等解析出来。

# 练习
#
# 找一个网页，例如https://www.python.org/events/python-events/，
# 用浏览器查看源码并复制，然后尝试解析一下HTML，输出Python官网发布的会议时间、名称和地点。


data = '''

'''

parser = MyHtmlParser()
parser.feed(data)
