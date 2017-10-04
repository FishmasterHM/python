# -*- coding:utf-8 -*-
# 第 0014 题： 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：# student.txt (实为JSON字符串)
import xlwt
import json

def DataRead(path):
    ifile = open(path, 'r').read()
    text = json.loads(ifile)
    # dumps, loads针对内存内容; dump, load针对外部内容
    return text

def XmlWrite(text, opath):
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('student', cell_overwrite_ok=True)
    st_text = sorted(text.iteritems(), key = lambda x:x[0])
    row = 0
    font = xlwt.Font()
    font.name = 'Times New Roman'             # font name
    font.underline = True
    style = xlwt.XFStyle()
    style.font = font
    style.num_format_str = '##0.00'
    for key, value in st_text:
        col = 0
        worksheet.write(row, col, float(key), style)
        for element in value:
            col += 1
            worksheet.write(row, col, element)
        row += 1

    workbook.save(opath)

if __name__ =='__main__':
    ipath = 'student.txt'
    text = DataRead(ipath)
    outpath = 'student.xls'
    XmlWrite(text, outpath)
