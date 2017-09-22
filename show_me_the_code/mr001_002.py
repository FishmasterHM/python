# -*- coding:utf-8 -*-

#第 0001 题：**做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用**生成激活码**（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）
#by Hanmi

import random
import string
import MySQLdb as MS


ilist = range(48,58,1)+range(65,91,1)+range(97,123,1)
for n in range(0,len(ilist)):
    ilist[n] = chr(ilist[n])


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

# 储存到sql
    conn = MS.connect(host="localhost", user="root", passwd="i2hguhi8")
    cursor = conn.cursor()        #

    sqlcmd = "CREATE DATABASE IF NOT EXISTS test01;"
    cursor.execute(sqlcmd)
    sqlcmd = "USE test01;"
    cursor.execute(sqlcmd)
    sqlcmd = "CREATE TABLE IF NOT EXISTS actcode("\
                +"id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,"\
                +"ActCode varchar(80) NOT NULL) AUTO_INCREMENT=1;"
    cursor.execute(sqlcmd)
    for code in result:
        cursor.execute("INSERT INTO actcode(ActCode) VALUES(%s)", [code])
        print cursor.lastrowid    # check last autoincrement
    conn.commit()
    cursor.close()
    conn.close()

# 规范的SQL写法
"""    
try:
    sursor.execute(....)
except MySQLdb.ERROR, e:
    print "MySQL Error %d: %s" % (e.args[0], e.args[1])
    conn.rollback()

conn.commit
"""
"""
执行SELECT后可用 cursor.fetchone()/fetchall() 查询
