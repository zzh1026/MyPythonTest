#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 注释 '

__author__ = 'zzh'

#
# Pillow
#
# PIL：Python Imaging Library，已经是Python平台事实上的图像处理标准库了。PIL功能非常强大，但API却非常简单易用。
#
# 安装命令
# $ pip install pillow
# 如果遇到Permission denied安装失败，请加上sudo重试。

# 操作图像
#
# 1, 图像缩放操作
from PIL import Image

# 打开一个jpg图像文件，当前路径
im = Image.open('test.jpg')

# 获得图像尺寸
w, h = im.size
print('Original image size: %s x %s' % (w, h))

# 缩放到50%
im.thumbnail((w // 2, h // 2))
print('Resize image to: %s x %s' % (w // 2, h // 2))

# 把缩放后的图像用jpeg格式保存
# im.save('new.jpg', 'jpeg')
# im.show()


# 其他功能如切片、旋转、滤镜、输出文字、调色板等一应俱全。
#
# 2, 模糊效果
from PIL import ImageFilter

# 打开文件
im = Image.open('test.jpg')
# 应用模糊滤镜
im2 = im.filter(ImageFilter.BLUR)
# 保存结果
im2.save('blur.jpg', 'jpeg')

# 3, PIL的ImageDraw提供了一系列绘图方法，让我们可以直接绘图。
#
# 生成字母验证码图片,这是生成一个图片的
from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random


# 随机字母
def rndChar():
    return chr(random.randint(65, 90))


# 随机颜色 ,返回一个含有 rgb 三色的 tuple
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


# 240 x 60:
width = 60 * 4
height = 60

# 创建一个纯白的 限定大小的 image
image = Image.new('RGB', (width, height), (255, 255, 255))

# 创建Font对象, 设置字体的效果和 大小
font = ImageFont.truetype('arialbi.ttf', 36)
# font = ImageFont.truetype('DejaVuSerif.ttf', 36)
# font = ImageFont.load_default()


# 创建Draw对象:
draw = ImageDraw.Draw(image)

# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())

# 输出文字
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), fill=rndColor2(), font=font)

# 模糊
image = image.filter(ImageFilter.BLUR)

# 保存
image.save('autocode.jpg', 'jpeg')

# Pillow官方文档
#
# https://pillow.readthedocs.io/en/latest/
#
# 代码:
# https://github.com/michaelliao/learn-python3/blob/master/samples/packages/pil/use_pil_resize.py
