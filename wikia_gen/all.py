#  -*- coding: utf-8 -*-
import gen_info,gen_attacks,gen_statistics,gen_cost
import wikia

def show_all(name):
	print wikia.construction()
	gen_info.show(name)
	print wikia.overview()
	gen_attacks.show(name)
	gen_statistics.show(name)
	gen_cost.show(name)
	print wikia.updates()
	print wikia.unitbox()

if __name__ == '__main__':
	unit_name = 's_arctic_trooper'
	show_all(unit_name)
