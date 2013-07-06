#  -*- coding: utf8 -*-

# 相关设定，
# 请在第一次运行之前设定好json文件的路径，在def path()中，使用‘/’分隔文件夹，现有值仅作为参考
#如果想生成不同版本的PV表，请指定版本，在def version()中指定


# 公用部分

# 指定BN版本，将做为PV表文件的后缀
# specify the version of the game, it will be used as a postfix of the generated file.
def version():
	return '2.98'

# 请指定json文件的路径
# specify the path of your json file
def path():
	return 'D:/Games/BN/local/bundle/'+version()+'/bundle/'

# 获取作战单位（BattleUnits）文件的路径
# return the json file path of BattleUnits.json
def json_unit():
	return path()+'BattleUnits.json'

# PV相关部分

# 指定要生成PV表的语言，目前仅支持中文和英文，默认为中文，如果要生成英文，请将下面的'ch'改为'en'
# select your prefered language of generated PV table. 'en' for English, 'ch' for Chinese,
def lang():
	return 'ch'

# output file path
def file_out():
	return '../PV_files/pv_' + version() + lang()

# output track file path
def pv_track_path():
	return '../PV_files/pv_track_' + version() + lang()


# 玩家兵种的最高等级
# return the max rank of player units
def max_rank():
	return 6

# 模板文件分隔符，默认为'='
# template seperator, default: '='
def sep_template():
	return '='

# 输出分隔符，默认为Tab
# output seperator, default: Tab
def sep_out():
	return '\t'

# !!function name is somewhat bad
# 打开PV值模板文件
# open the template file
def pv_template():
	return open('../resources/nameMap_'+lang()+'.txt')




# Wiki部分

# 获取作战技能（BattleAbilities.json）文件的路径
# return the json file path of Units
def json_abilities():
	return path()+'BattleAbilities.json'


# 指定wiki的模板
def wiki_template():
	print 'not implemented'
	pass