#  -*- coding: utf-8 -*-

# Battle nations（战场争锋） 新单位检测器
# 作者： 囧泥
# 协议：WTFPL 2.0


#output format unit id + icon name(for searching images)

import json,sys
sys.path.append("..")
from shared import settings
from pprint import pprint

version   = settings.version()
json_path = settings.json_unit()
max_rank  = settings.max_rank()
data      = json.load(file(json_path))
template  = settings.pv_template()
lines     = template.readlines()
sep_t     = settings.sep_template()

def new_unit_list():
    result = []
    for unit_id in data.keys():
        if data[unit_id]["side"] == "Player":
            if len(data[unit_id]["stats"]) == max_rank:
                if not known(unit_id):
                    result.append((str)(unit_id+' '+data[unit_id]['icon'][0:-5]))# remove _icon
    return result

def known(unit_id):
    for line in lines:
        if len(line) <= 1:
            continue
        current_id = line.split(sep_t)[1][0:-1]
        if unit_id == current_id:
            return True
    return False

if __name__ == '__main__':
    pprint(new_unit_list())
