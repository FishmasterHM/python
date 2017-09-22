# -*- coding:utf-8 -*-
# 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示
# 效果。 类似于图中效果

from PIL import Image
from PIL import ImageDraw as ID
from PIL import ImageFont as IF

im = Image.open("fig/dolphin_before.jpg")
print "format: " + im.format  
print "size: ", im.size
print "mode: ", im.mode
drawim = ID.Draw(im)
xsize, ysize = im.size
fontsize = 80                               # determine the size of font
#https://stackoverflow.com/questions/4902198/pil-how-to-scale-text-size-in-relation-to-the-size-of-the-image
# 关于fontsize 和图片大小的关系
myFont = IF.truetype("fig/FreeMono.ttf",   # 字体
                     fontsize)

drawim.text([0, 0.], "5",
             fill = (255, 0, 0), font = myFont)
im = im.transpose(Image.FLIP_TOP_BOTTOM)
im.save("fig/dolphin_after.jpg")



#box = (50, 50, 427, 371)                  # (左上到右下,横坐标,纵坐标)
#region = im.crop(box)                     # 剪切
# Image.transpose(method) 
# Image.transpose(FLIP_LEFT_RIGHT), Image.ROTATE_180
# http://www.cnblogs.com/wei-li/archive/2012/04/19/2456725.html
#region = region.transpose(Image.FLIP_TOP_BOTTOM)
#im.paste(region,box)
