# -*- coding:utf-8 -*-

# 第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数。
import re

def fileprocesser(fname):
    file = open(fname,'r')
    text = file.read().lower() 
    pattern = re.compile(r'\b[a-z]+\b', re.M)
    data = pattern.findall(text)
    return data

def wdcounter(data):
    # creat new dict
    wdstat = {}
    for word in data:
        if word in wdstat:
            wdstat[word] += 1
        else:
            wdstat[word] = 1
    print wdstat

if __name__ == '__main__':
    data = fileprocesser('04.txt')
    wdcounter(data)
