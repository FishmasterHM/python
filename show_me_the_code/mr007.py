# -*- coding:utf-8 -*-

# 第 0007 题：有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。

import glob
import re
#import codecs

def Counter(ipath):
    pattern = re.compile(r'\w+\.py')
    fname = ''.join(pattern.findall(ipath))
    ltotal = 0
    lcommand = 0
    lnote = 0
    lblank = 0
    note_flag = False
    f = open(ipath,  'r')
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if line.startswith('\"\"\"') or line.startswith("\'\'\'"):
            if not note_flag and not (line.endswith('\"\"\"') or 
                                      line.endswith("\'\'\'")):
                '''if statement is too long, so written separetely'''
                lnote += 1
                note_flag = True
                continue
            elif line.endswith('\"\"\"') or line.endswith("\'\'\'"):
                lnote += 1
                continue
        if line.endswith('\"\"\"') or line.endswith("\'\'\'"):
            if note_flag:
                lnote += 1
                note_flag = False
                continue       
        if line.startswith('#') or note_flag:
            lnote += 1
        elif len(line) == 0:
            lblank += 1
        else:
            lcommand += 1
    ltotal = lnote + lcommand + lblank
    ltest = len(lines)
    print ('for file %s ==> commands: %s, notes: %s, blank: %s,' 
          +' total: %s, tt: %s') % (fname, lcommand, lnote, lblank, ltotal, ltest)       
  
      
def Engine(path):
    files = glob.glob(path)
    for file in files:
        Counter(file)
        exit(1)





if __name__ == '__main__':
    path = '/home/hank/python/execises/*.py'
    Engine(path)
