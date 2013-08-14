#  -*- coding: utf-8 -*-

# Battle nations（战场争锋） PV生成器
# 作者：囧泥
# 协议：WTFPL 2.0


import sys, json
sys.path.append("..")
from shared import settings
# 如果希望输出xsl格式，删除下面一行的 '#' 以及最后一行的 '#'
#import xlwt

version   = settings.version()
json_path = settings.json_unit()
max_rank  = settings.max_rank()
data      = json.load(file(json_path))
template  = settings.pv_template()
lines     = template.readlines()
file_out  = settings.file_out()
sep_t     = settings.sep_template()
sep_out   = settings.sep_out()

def pv_line(line):
    unit_id     = line.split(sep_t)[1][0:-1]#remove \n
    # localized_name unit_id
    current_pvs = line[0:-1].replace(sep_t,sep_out) #remove \n, replace '=' with ' '
    if unit_id not in data.keys():#id不在json文件里，可能是模板比json要新，在生成老版本PV表时可能出现
        return ''
    ranks = len(data[unit_id]['stats'])
    for rank in xrange(0,ranks):
        current_pvs += sep_out + str(data[unit_id]['stats'][rank]['pv'])
    current_pvs += '\n'
    return current_pvs

def pv_out_cli():
    for line in lines:
        if len(line) <= 1:#empty lines
            print ''
            continue
        current_pv_line = pv_line(line)
        if len(current_pv_line) > 0:
            print current_pv_line,

def pv_out_txt():
    out_path = file_out + '.txt'
    out      = open(out_path,'w')
    for line in lines:
        if len(line) <= 1: #empty lines
            out.write('\n')
            continue
        current_pv_line = pv_line(line)
        if len(current_pv_line) > 0:
            out.write(current_pv_line)
    out.close()

# 因输出中文乱码问题尚未解决，所以暂未实现
def pv_out_csv():
    pass

# for online displaying on Github
def pv_out_md():
    out_path = file_out + '.md'
    out      = open(out_path,'w')
    out.write('<table>\n')
    for line in lines:
        if len(line) <= 1: #empty lines
            continue
        out.write('<tr>')
        current_pv_line = pv_line(line)[0:-1]
        if len(current_pv_line) > 0:
            sp = current_pv_line.split(sep_out)
            for x in sp:
                out.write('<td>' + x + '</td>')
        out.write('</tr>\n')
    out.write('\n</table>')
    out.close()

def pv_out_xls():
    book     = xlwt.Workbook(encoding = 'utf-8')
    pv_sheet = book.add_sheet('pv' + version)

    # too ugly....looking for a better solution
    style_name_0 = xlwt.easyxf('pattern: pattern solid, fore_colour silver_ega;'
                    'borders: left thin, right thin, top thin, bottom thin;'
                    'font: name SimSun, colour black, height 240, bold True;')

    style_name_1 = xlwt.easyxf('pattern: pattern solid, fore_colour ice_blue;'
                        'borders: left thin, right thin, top thin, bottom thin;'
                        'font: name SimSun, colour black, height 240, bold True;')

    style_id_0 = xlwt.easyxf('pattern: pattern solid, fore_colour silver_ega;'
                        'borders: left thin, right thin, top thin, bottom thin;'
                        'font: colour black, height 200;')

    style_id_1 = xlwt.easyxf('pattern: pattern solid, fore_colour ice_blue;'
                        'borders: left thin, right thin, top thin, bottom thin;'
                        'font: colour black, height 200;')

    style_pv_0 = xlwt.easyxf('pattern: pattern solid, fore_colour silver_ega;'
                        'borders: left thin, right thin, top thin, bottom thin;'
                        'font: name SimSun, colour dark_blue, height 240, bold True;')

    style_pv_1 = xlwt.easyxf('pattern: pattern solid, fore_colour ice_blue;'
                        'borders: left thin, right thin, top thin, bottom thin;'
                        'font: name SimSun, colour black, height 240, bold True;')
    row        = 0
    style_name = style_name_0
    style_id   = style_id_0
    style_pv   = style_pv_0

    for line in lines:
        if len(line) <= 1:#empty lines
            row += 1
            continue

        style_name = style_name_0 if style_name == style_name_1 else style_name_1
        style_id =  style_id_0 if style_id == style_id_1 else style_id_1
        style_pv =  style_pv_0 if style_pv == style_pv_1 else style_pv_1

        unit_name = line.split(sep_t)[0]
        unit_id = line.split(sep_t)[1][0:-1]

        unit_valid = unit_id in data.keys()
        #print name
        if unit_valid:
            pv_sheet.write(row, 0, unit_name, style_name)
            pv_sheet.write(row, 1, unit_id, style_id)

            ranks = len(data[unit_id]['stats'])
            for rank in xrange(0,ranks):
                pv_sheet.write(row, rank + 2, data[unit_id]['stats'][rank]['pv'], style_pv)
            row += 1
    book.save(file_out + '.xls')

if __name__ == '__main__':
    pv_out_cli()
    pv_out_txt()
    pv_out_md()
    #pv_out_xls()
