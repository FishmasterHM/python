# -*- coding:utf-8 -*-

#第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

import os
from PIL import Image as Img
import glob

def picresizer(path):
    files = glob.glob(path)
    print files
    for pic in files:
        im = Img.open(pic)
        ph, pw = im.size
        

if __name__ == '__main__':
    path = '/home/hank/python/excises/fig/*'
    picresizer(path)
