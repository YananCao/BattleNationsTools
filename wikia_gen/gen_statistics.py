#  -*- coding: utf-8 -*-
import json,sys
sys.path.append("..")
import wikia,tools
from shared import settings

attribute_list = wikia.attribute_list()
attribute_map  = wikia.attribute_map()
resource_map   = wikia.resource_map_promote()
time_list      = wikia.up_time_list()
version        = settings.version()
json_path      = settings.json_unit()
maxrank        = settings.max_rank()
data           = json.load(file(json_path))
comma          = tools.intWithCommas

def get_data(name):
	for att in attribute_list:
		for rank in xrange(0,maxrank):
			if att not in data[name]['stats'][rank].keys():
				continue
			if att == 'levelUpCost':
				get_lv_up_cost(name,rank)
			else:
				print_data(name,att,rank,data[name]['stats'][rank][att])

def print_data(name,att,rank,value):
	statistics_template = wikia.statistics_general()
	offset = 1 if att != 'levelCutoff' else 2
	current_unit_state = data[name]['stats'][rank]
	num_data = current_unit_state[att]
	# if num_data == 0:# 不输出为0的项
		# return
	if att != 'hp' and att != 'armorHp':
		num_data = comma(num_data)
	print statistics_template.format(attribute_map[att],rank+offset,num_data)

def get_lv_up_cost(name,rank):
	u_time_gold  = wikia.statistics_time_gold()
	res_temp     = wikia.statistics_resource()
	u_resource   = ''
	cost         = data[name]['stats'][rank]['levelUpCost']
	u_time_gold  = u_time_gold.format(lvl=rank+2,time=time_list[rank],gold=comma(cost['money']))

	check_rare_res(cost,cost.keys())
	resources = cost['resources']

	for key in resources.keys():
		if resources[key]>0:
			u_resource += res_temp.format(res=resource_map[key],num=comma(resources[key]))

	print u_time_gold+u_resource

def check_rare_res(cost,keys):#usually not need
	for key in keys:
		if isinstance(cost[key],int) and cost[key]>0 and key!='money':#output others if not 0
			print "Unusual resources needed!!!"
			print key,
			print cost[key]
			sys.exit(0)

def show(name):
	print wikia.statistics_start()
	get_data(name)
	print wikia.statistics_end()

if __name__ == '__main__':
	#unit_name = raw_input('NAME: ')
	unit_name = 's_arctic_trooper'
	show(unit_name)
