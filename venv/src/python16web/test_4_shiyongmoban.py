#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 注释 '

__author__ = 'zzh'

#
# 使用模板
#
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('test_4_home.html')


@app.route('/singin', methods=['GET'])
def singin_form():
    return render_template('test_4_form.html')


@app.route('/singin', methods=['POST'])
def singin():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
        return render_template('test_4_singin_ok.html', username=username)
    return render_template('test_4_form.html', message='Bad username or password', username=username)


if __name__ == '__main__':
    app.run()

#
# 在Jinja2中，用{% ... %}表示指令表示循环、条件判断等指令语句
#
# 比如循环输出页码
# {% for i in page_list %}
#     <a href="/page/{{ i }}">{{ i }}</a>
# {% endfor %}
