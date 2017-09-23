# -*- coding:utf-8 -*-

#第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率(1136*640)的大小。

import os
from PIL import Image as Img
import glob

def picresizer(path):
    files = glob.glob(path)
    for pic in files:
        im = Img.open(pic)
        ph, pw = im.size
        ratio = min(1136./ph, 640./pw)
        if ratio < 1.0:
            print int(ph*ratio), int(pw*ratio)
            out_im = im.resize((int(ph*ratio), int(pw*ratio)))
            out_im.save(pic)
            
        

if __name__ == '__main__':
    path = '/home/hank/python/project/show_me_the_code/fig/*'
    picresizer(path)
