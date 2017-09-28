# -*- coding:utf-8 -*-

# 一个HTML文件，找出里面的正文。
# ref: http://cuiqingcai.com/1319.html

import urllib2
from bs4 import BeautifulSoup
import re

def findtext(url):
    #resp = urllib2.urlopen(url)
    resp = open(u'./url4ex8/shandian.html', 'r')
    soup = BeautifulSoup(resp, 'lxml')
    texts = soup.find_all('div', {"class":"para"})
    out = []
    for content in texts[:]:
        sp = content.span
        if sp != None:
            content.span.extract()     
            # still buggy, when span isn't a child of div
        data = content.text.encode('utf-8')
        data = str(data)
        data = "".join(line.strip() for line in data.split("\n"))
        # remove all white space (l,r,m)
        if data != '':
            out.append(data)
    return out





if __name__ == '__main__':
    url = u'https://baike.baidu.com/item/%E9%97%AA%E7%94%B5/16990'
    text = findtext(url)
    a = 1
    for line in text:
        print a, line.decode('string_escape')
        a += 1
