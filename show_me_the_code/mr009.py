# -*- coding:utf-8 -*-

# 第 0009 题： 一个HTML文件，找出里面的链接。

import urllib2
from bs4 import BeautifulSoup
import re

def engine(url):
    request = urllib2.Request(url)
    resp = urllib2.urlopen(request)
    doc = resp.read()
    soup = BeautifulSoup(doc, 'lxml')
    for link in soup.find_all('a', attrs={'href':re.compile(r'^http:')}):
         print link.get('href')

if __name__ == '__main__':
    url = u'http://www.163.com'
    engine(url)
