#  -*- coding: utf8 -*-
import sys
sys.path.append("..")
from shared import settings
#formats about wikia

#construction
def construction():
	return '{{Construction}}'

#overview
def overview():
	return '==Overview==\n'+clear()

#unit info
def info():
	return '{{{{StaticUnitInfoBox\n\
| image         = \n\
| name          = \n\
| shortname     = \n\
| ut            = {type}\n\
| ul            = {level}\n\
| other_b       = {req_b}\n\
| blocking      = {blocking}\n\
| gametag       = {name}\n\
}}}}'

def rank1_info():
	return '{{{{Rank1UnitInfobox\n\
| hp            = {hp}\n\
| armor         = {armor}\n\
| defense       = {defense}\n\
| offense       = {offence}\n\
| dmgtype       = {{{{{dmgtype}}}}}\n\
| mindmg        = {mindmg}\n\
| maxdmg        = {maxdmg}\n\
| range         = {range}\n\
| lof           = {lof}\n\
| notes = \n\
}}}}'

#attacks
def attacks_start():
	return '==Attacks==\n'




#statistics
def statistics_general():
	return '|{}{} = {}'

def statistics_time_gold():
	return '|pc{lvl} = {{{{Time|{time}}}}}<br>{{{{Gold|{gold}}}}}'

def statistics_resource():
	return '<br>{{{{{res}|{num}}}}}'

def statistics_start():
	return '==Statistics==\n{{UnitRanksBox'
def statistics_end():
	return '|notes = \n}}\n<!--Values up-to-date as of '+ settings.version()+'.-->\n'+clear()


#attributes
def attribute_list():
	return ['levelCutoff','hp','armorHp','bravery','defense','dodge','critical','abilitySlots','levelUpCost','pv']

def attribute_map():
	#json:wikia
	return {'hp':'hp','armorHp':'armor','levelCutoff':'sp','bravery':'bravery',\
			'defense':'defense','dodge':'dodge','critical':'crit','abilitySlots':'ability',\
			'levelUpCost':'pc','pv':'uv'}
def blocking_map():
	#json:wikia
	return {'0':'None','1':'Partial','2':'Blocking'}
def lof_map():
	#json:wikia
	return {'0':'Contact','1':'Direct','2':'Precise','3':'Indirect'}

#resources
def resource_map_promote():
	#json:wikia
	return {'steel':'Steel','wood':'Wood','bars':'Bars','oil':'Oil','gear':'Gears',\
		'skull':'Skulls','concrete':'Concrete','stone':'Stone','tooth':'Teeth',\
		'sbars':'Laurels','coal':'Coal','lumber':'Lumber','iron':'','sgear':'Widgets',\
		'sskull':'Powder','stooth':'Necklaces'}

def resource_map_cost():
	#json:wikia
	return {'steel':'steel','wood':'wood','bars':'bars','oil':'oil','gear':'gears',\
		'skull':'skulls','concrete':'concrete','stone':'stone','tooth':'teeth',\
		'sbars':'laurels','coal':'coal','lumber':'lumber','iron':'iron','sgear':'widgets',\
		'sskull':'powder','stooth':'necklaces','currency':'nanopods','z2points':'z2points',\
		'money':'gold','heart':'merits','star':'stars'}

def up_time_list():
	return ['14400','43200','86400','172800','172800']

#costs
def cost_general():
	return '|{} = {}'

def cost_start():
	return '==Cost==\n{{BuildCost'

def cost_heal_start():
	return '{{HealCost'

def end():
	return '}}\n'

def clear():
	return '{{clear}}\n'

def end_clear():
	return end()+clear()

def updates():
	return '==Updates==\n'+clear()


def unitbox():
	return '{{UnitBox}}'
