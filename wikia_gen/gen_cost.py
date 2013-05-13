#  -*- coding: utf8 -*-
import json,sys
import wikia,tools
sys.path.append("..")
from shared import settings

resource_map  = wikia.resource_map_cost()
json_unit     = settings.json_unit()
data          = json.load(file(json_unit))
cost_template = wikia.cost_general()

def get_cost(name):
	unit = data[name]
	tags  = unit['tags']
	cost  = unit['cost']

	building = '???'
	# building = 'hospital' if 'Hospital' in tags else 'vehicle'
	print cost_template.format('building',building)
	print cost_template.format('time',unit['buildTime'])
	print_cost(name,'cost')

def get_cost_heal(name):
	unit = data[name]
	tags = unit['tags']

	building = 'hospital' if 'Hospital' in tags else 'vehicle'
	print cost_template.format('building',building)
	print cost_template.format('time',unit['healTime'])
	print_cost(name,'healCost')

def print_cost(name,cost_type):#id = healCost or cost
	cost = data[name][cost_type]
	for key in cost:
		if key == 'resources':
			continue
		if cost[key]>0:
			print cost_template.format(resource_map[key],cost[key])

	resources = cost['resources']
	for key in resources.keys():
		if resources[key]>0:
			print cost_template.format(resource_map[key],resources[key])


def show(name):
	print wikia.cost_start()
	get_cost(name)
	print wikia.end()
	print wikia.cost_heal_start()
	get_cost_heal(name)
	print wikia.end_clear()

if __name__ == '__main__':
	unit_name = 's_trooper_bigGameHunter'
	show(unit_name)
