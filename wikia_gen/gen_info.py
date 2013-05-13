#  -*- coding: utf-8 -*-
import json, sys
import wikia
sys.path.append("..")
from shared import settings


json_unit      = settings.json_unit()
json_abilities = settings.json_abilities()
data_unit      = json.load(file(json_unit))
data_ability   = json.load(file(json_abilities))
blocking_map   = wikia.blocking_map()
lof_map        = wikia.lof_map()

def show(name):
	show_info(name)
	show_rank1_info(name)

def show_info(name):
	info = wikia.info()
	unit = data_unit[name]
	req = ''
	for key in unit['prereq']:
		if 'compositionName' in unit['prereq'][key].keys():
			req += unit['prereq'][key]['compositionName']+' '


	unit_type = ''
	for key in unit['tags']:
		if key == 'Hospital' or key == 'VRB':
			break
		unit_type += key+'-'

	print info.format(type = unit_type[0:-1],\
						level = unit['prereq']['1']['level'],\
						req_b = req,\
						blocking = blocking_map[str(unit['blocking'])],\
						name = name)

def show_rank1_info(name):

	rank1_info = wikia.rank1_info()
	unit = data_unit[name]
	rank1 = unit['stats'][0]
	hp = rank1['hp']
	armor = '' if 'armorHp' not in rank1.keys() else rank1['armorHp']
	defense = rank1['defense']

	weapon1 = unit['weapons']['primary']
	weapon_stats = weapon1['stats']
	ability1 = weapon1['abilities'][0]
	ability_stats = data_ability[ability1]['stats']
	offence = ability_stats['attack']
	dmgtype = ability_stats['damageType'][0]
	mindmg = weapon_stats['base_damage_min']
	maxdmg = weapon_stats['base_damage_max']
	r1 = ability_stats['minRange']
	r2 = ability_stats['maxRange']
	lof = lof_map[str(ability_stats['lineOfFire'])]
	print rank1_info.format(hp = hp,\
							armor = armor,\
							defense = defense,\
							offence = offence,\
							dmgtype = dmgtype,\
							mindmg = mindmg,\
							maxdmg = maxdmg,\
							range = str(r1)+'-'+str(r2),\
							lof = lof
							)

if __name__ == '__main__':
	unit_name = 'veh_pickup_catapult'
	show(unit_name)
