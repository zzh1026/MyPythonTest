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
    print('show main')
    return render_template('uploadfile.html')


# 具体展示图片
def upload():
    # 处理上传文件
    print('调用到upload()方法')
    filedata = request.files['fileField']
    if filedata:
        file_name = 'C:\\Users\\zhaozehui\\PycharmProjects\\PythonTest\\venv\\src\\python19webapp2\\datas\\' + filedata.filename
        filedata.save(file_name)  # 上传文件写入
        return '{"msg": "上传成功！"}'
        # try:
        # except IOError:
        #     return '上传文案件失败'
        # return '上传文件成功,文件名: %s' % file_name
    else:
        return '{"msg": "请上传文件！"}'
    pass


@app.route('/background_process_test')
def proccessData():
    buchang = request.form['buchang']
    title_name = request.form['title_name']
    print(buchang, title_name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='12316')
