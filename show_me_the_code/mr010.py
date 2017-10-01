# -*- coding:utf-8 -*-
#第 0010 题： 使用 Python 生成类似于下图中的字母验证码图片
import random as RD
import string
from PIL import Image
from PIL import ImageDraw as ID
from PIL import ImageFont as IF
from PIL import ImageFilter


def CharDefiner(num):
    char = list(string.digits+string.letters)
    letters = RD.sample(char, num)
    letters = ''.join(letters)
    return letters

def rdcolor(full=True):
    if full == True:
        return (RD.randint(0,255), RD.randint(0,255), RD.randint(0,255))
    else:
        return (RD.randint(30,130), RD.randint(30,130), RD.randint(30,130))

def draw_line(draw, width, height):
    begin = (RD.randint(0, width), RD.randint(0, height))
    end = (RD.randint(0, width), RD.randint(0, height))
    draw.line([begin,end], fill=rdcolor())

def Create_verification_code(text, font, numline=6,
                             width=300, height=150,
                             ):
    bg_color = (255,255,255)
    im = Image.new('RGB', (width, height), bg_color)
    draw = ID.Draw(im)
    for wd in range(width):
        for ht in range(height):
            if 0.1 < RD.random():
                draw.point((wd, ht), fill = rdcolor(full=False))

    myfont = IF.truetype(font, 80)
    w, h = myfont.getsize(text)
    ltext = len(text)
    x = (width - w)/(ltext+1)
    dx = x + w/ltext 
    y = (height -h)/2
    for c in text:
        draw.text([x,y], c, fill=rdcolor(), font=myfont)
        x += dx
    for k in range(numline):
        draw_line(draw, width, height)
    im = im.filter(ImageFilter.SMOOTH_MORE)
    im = im.filter(ImageFilter.BLUR)
    # http://blog.csdn.net/guduruyu/article/details/71404941
    im.show()


if __name__ == '__main__':
    num = 4
    font = 'FreeMono.ttf'
    text = CharDefiner(num)
    Create_verification_code(text, font)
