#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# 学习专用
from xlutils.copy import copy
import xlwt, xlrd

# 写入文件部分
# book = xlwt.Workbook(encoding='utf-8', style_compression=0)
#
# sheet = book.add_sheet('test',cell_overwrite_ok=True)
#
# sheet.write(0, 0, 'EnglishName')
#
# sheet.write(1, 0, 'Marcovaldo')
#
# txt1 = '中文名字'
#
# sheet.write(0, 1, txt1)
#
# txt2 = '马可瓦多'
#
# sheet.write(1, 1, txt2)
#
# book.save(r'/root/book1.xlsx')

# ========================================================

# 读取文件部分内容
# xlsfile = r'/root/kaoqin.xlsx'
#
# bookkq = xlrd.open_workbook(xlsfile)
#
# sheet0 = bookkq.sheet_by_index(0)
#
# print(sheet0)
#
# sheet_name = bookkq.sheet_names()[0]
#
# print(sheet_name)
#
# sheet1 = bookkq.sheet_by_name(sheet_name)
#
# nrows = sheet0.nrows
#
# print(nrows)
#
# for i in range(nrows):
#     print(sheet1.row_values(i))


# ==============================================================

xlsfile = r'/root/kaoqin.xls'

bookkq = xlrd.open_workbook(xlsfile, formatting_info=True)


sheet0 = bookkq.sheet_by_index(0)


sheet_name = bookkq.sheet_names()[0]


sheet1 = bookkq.sheet_by_name(sheet_name)

nrows = sheet0.nrows

for i in range(5, nrows-2):
    print(sheet1.row_values(i))


# str_up = sheet1.row_values(5)[4]
# str_down = sheet1.row_values(6)[4]
#
# if str_up == r'√' and str_down == r'旷':
#     str_up = r'>'
#
# if str_up == r'旷' and str_down == r'√':
#     str_down = r'<'
#
# print(str_up)
# print(str_down)


# =================================================
# row_len = len(sheet1.row_values(5))
#
# for i in range(4, row_len-10):
#     print(sheet1.row_values(5)[i], end=' ')
# print('')
# for i in range(4, row_len - 10):
#     print(sheet1.row_values(6)[i], end=' ')
#
# for i in range(4, row_len-10):
#     if sheet1.row_values(5)[i] == r'√' and sheet1.row_values(6)[i] == r'旷':
#         sheet1.row_values(5)[i] = r'>'
#     if sheet1.row_values(5)[i] == r'旷' and sheet1.row_values(6)[i] == r'√':
#         sheet1.row_values(5)[i] = r'<'


# 更改EXCEL部分
bookTag = copy(bookkq)

sheetTag = bookTag.get_sheet(0)

# sheetTag.write(0, 0, '第一行，第一列')
# sheetTag.write(0, 1, '第一行，第二列')

# 循环
row_len = len(sheet1.row_values(5))

for r in range(5, nrows-2, 2):
    for i in range(4, row_len-10):
        tag = sheet1.row_values(r)[i]
        if sheet1.row_values(r)[i] == r'√' and sheet1.row_values(r+1)[i] == r'旷':
            tag = r'>'
        if sheet1.row_values(r)[i] == r'旷' and sheet1.row_values(r+1)[i] == r'√':
            tag = r'<'
        sheetTag.write(r, i, tag)

bookTag.save(r'/root/demo.xls')



