# -*- coding:utf-8 -*-

#第 0001 题：**做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用**生成激活码**（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）
#by Hanmi

import random
import string
import MySQLdb

conn = MySQLdb.connect(host="localhost", user="root",
                       passwd="i2hguhi8", db="test1",
                       port=3306, charset="utf8")

ilist = range(48,58,1)+range(65,91,1)+range(97,123,1)
for n in range(0,len(ilist)):
    ilist[n] = chr(ilist[n])

print ilist

def generator(num, len=16):
    """16位激活码"""
    result = []
    i = 01   
    while (i <= num):
        ma = ''.join(random.sample(ilist,len))
        if ma not in result:
            result.append(ma)
            i += 1
        else:
            pass
    return result



if __name__ == '__main__':
    result = generator(35)
    print result
    
    # 储存到sql
    cur = conn.cursor()
    for k in range(0, len(result)):
        param = result[k]
    cur.executemany("replace into ActCode(Code) values (%s)",result)
    conn.commit()
