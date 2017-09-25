# -*- coding:utf-8 -*-

# 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，
# 请统计出你认为每篇日记最重要的词。

import re
import glob

def dataprocesser(path):
    files_path = glob.glob(path)
    file_data = []
    file_name = []
    for file in files_path:
        ifile = open(file, 'r')
        text = ifile.read().lower()
        pattern = re.compile(r'\b[a-z]+\b', re.M)
        pattern_fname = re.compile(r'\d+\.txt$')
        fname = pattern_fname.findall(file)
        data = pattern.findall(text)
        file_name.append(fname)
        file_data.append(data)
        ifile.close()
    return file_name, file_data

def wordcounter(name, data):
    ignore_list = ['to', 'be', 'is', 'the', 'and', 'of']
    keyword = {}
    for i in range(3):
        wddict = {}
        for word in data[i]:
            if word in wddict:
                wddict[word] += 1
            else:
                wddict[word] = 1
        top = sorted(wddict.iteritems(), key = lambda x:x[1], 
                     reverse = True)

        for n in range(len(wddict)):
            if top[n][0] not in ignore_list:
                oname = ''.join(name[i])
                keyword[oname] = ''.join(top[n][0])
                break
            else:
                pass
    return keyword
            


if __name__ == '__main__':
    path = '/home/hank/python/project/show_me_the_code/diaries/*.txt'
    name, data = dataprocesser(path)
    keywords = wordcounter(name, data)
    print keywords
