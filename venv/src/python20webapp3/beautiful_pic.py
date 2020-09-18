#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Created by zhaozehui at 2020/9/17

__author__ = 'zzh'

import os

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


# 显示所有文件夹
@app.route('/', methods=['GET', 'POST'])
def list_all():
    path = './static/mzitu/'
    all_pic = os.listdir(path)
    print(all_pic)
    return render_template('welcome.html', all_pic=all_pic)


# 具体展示图片
@app.route('/<path>', methods=['GET', 'POST'])
def list_pic(path):
    if (path not in os.listdir('./static/mzitu/')):
        return render_template('error.html')
    pic_path = './static/mzitu/' + path
    if os.path.isdir(pic_path):
        all_pic = os.listdir(pic_path)
        return render_template('pic.html', title=path, all_pic=all_pic)
    else:
        all_pic = os.listdir(pic_path)
        return render_template('welcome.html', all_pic=all_pic)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='12316')
