# -*- coding:utf-8 -*-

# 第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入 
# 敏感词语时，则打印出 Freedom，否则打印出 Human Rights。


# 第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户# 输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好
# 城市」。

def SensitiveWords(path):
    sf = open(path, 'r')
    swds = sf.read().split('\n')
    del swds[-1]
    return swds

def Engine_Ex11(swords):
    itext = raw_input('please enter your sentances >')
    lwords = len(swords)
    counter = 0
    for swd in swords:
        if swd in itext:
            print 'Freedom'
            break
        counter += 1
        if counter == len(swords):
            print 'Human Rights'
    return None

def Engine_Ex12(swords):
    itext = raw_input('please enter your sentances >')
    for swd in swords:
        if swd in itext:
            itext = itext.replace(swd, '**')
            break
    print itext
    return None

if __name__ == '__main__':
    ipath = 'filtered_words.txt'
    swords = SensitiveWords(ipath)
    #Engine_Ex11(swords)
    Engine_Ex12(swords)
