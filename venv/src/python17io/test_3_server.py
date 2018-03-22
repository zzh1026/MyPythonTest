#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Created by zhaozehui at 2018/3/21

__author__ = 'zzh'

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/hello/meide', methods=['GET', 'POST'])
def singin():
    username = request.form['PATH_INFO']
    print(username)
    tem = render_template('welcome.html', username=username)
    return tem


if __name__ == '__main__':
    app.run()
