# -*- coding:utf-8 -*-

# 第 0013 题： 用 Python 写一个爬图片的程序，爬 这个链接里的日本妹子图片 :-)
import urllib2
import urllib
import re
import os

def GetPicAddress(url):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent': user_agent}
    req_body = ''
    try:
        req = urllib2.Request(url, headers = headers)
        resp = urllib2.urlopen(req)
        html_text = resp.read()
    except urllib2.URLError, e:
        if hasattr(e, 'code'):
            print e.code
        if hasattr(e, 'reason'):
            print e.reason
    
    pattern = re.compile('(?<=src=")http://imgsrc.baidu.com/forum/(?!pic\/item).+?\.jpg')
    items = re.findall(pattern, html_text)
    items = set(items)        #get only distinct pic addresses
    return items   
 
def DownloadPics(addresses, outpath):
    if os.path.isdir(outpath):
        print 'The output folder exists'
    else:
        os.makedirs(outpath) 
    x = 1
    for ads in addresses:
        urllib.urlretrieve(ads, outpath+'衫本有美'+str(x)+'.jpg')
        print 'Pic NO.'+str(x)+' finished'
        x += 1



if __name__ == '__main__':
    url = 'http://tieba.baidu.com/p/2166231880'
    adds = GetPicAddress(url)
    outpath = './Beauties/'
    DownloadPics(adds, outpath)
