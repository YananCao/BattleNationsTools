#  -*- coding: utf-8 -*-
# TODO incomplete function
import json, sys
import wikia
sys.path.append("..")
from shared import settings

json_unit      = settings.json_unit()
json_abilities = settings.json_abilities()
data_unit      = json.load(file(json_unit))
data_ability   = json.load(file(json_abilities))
lof_map        = wikia.lof_map()





def show(name):
	print wikia.attacks_start()


	print wikia.clear()





if __name__ == '__main__':
	unit_name = 'sw_guy_machete_player'
	show(unit_name)
