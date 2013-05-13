Battle Nations Tools
==================

>自己写的一些[Battle Nations(战场争锋)](http://www.z2.com/game/battle-nations)相关的小工具

- 作者：[囧泥](https://github.com/johnnywjy)
- 协议：[WTFPL 2.0](http://www.wtfpl.net/txt/copying/)

### 运行环境：

- python 2.x

### 支持的操作系统：

- 任何能运行python的系统，包括Windows，Linux，Mac OS

### 使用之前

- 检查是否安装了python，在cmd或terminal（终端）里输入`python --version`，如果显示类似`Python 2.7.3`则为已安装，如果显示命令未找到则需[下载python](http://python.org/download/)并安装

- 修改`shared`文件夹中的`settings.py`文件，文件内有说明

## Battle Nations PV生成器

> 从BattleUnits.json自动生成PV表的工具

### 使用说明

#### 使用之前

- 请先把cmd或terminal的当前路径设置到`pv_gen`文件夹路径

#### **PV生成器主程序**

- 运行 `python a_pvGen.py`，即可在`PV_files`文件夹生成格式为`pv_[版本][语言]`的PV表。默认为txt文件和cmd/terminal窗口输出，如果想生成`xsl`文件，请看[输出](#输出)部分

- 建议使用前运行 `python newUnitDetect.py` 来检测是否有未被名称翻译表（nameMap）收录的新单位，如果检测到新单位，则直接运行主程序不会生成这些新单位的PV。（原因： 为了生成的格式整齐，本程序无法生成不在nameMap文件中的单位PV资料，而nameMap尚未找到自动更新的方法）

#### **在线预览**

- 在`PV_files`文件夹中有以`.md`结尾的文件，如果你使用浏览器在Github上打开`pv_[版本号][语言].md`文件，可以直接查看表格。[点我查看示例](https://github.com/johnnywjy/BattleNationsTools/blob/master/PV_files/pv_2.85ch.md)

#### **名称翻译表——nameMap文件**

- 文件在`resources`文件夹下

- 文件名使用`nameMap_[语言].txt`的格式

- 内容使用`[兵种名称]   [id]`的格式，每个兵种占 1 行，使用`Tab`分隔

- 排列顺序和游戏中的显示顺序一致

- 不同建筑的单位之间有空行

#### **新单位检测**

- 运行`python newUnitDetect.py`

- 输出格式为`['[id]','[id]',...'[id]']`

- 示例 `['veh_artillery_napalm','s_bigfoot_child_player','s_laser_sniper']`

- 请手工修改nameMap文件，在其中加入这些`id`和对应语言的名称，格式参照前文。注意`名称`和`id`之间使用`Tab`分隔

- 如果检测结果是空的（输出结果为`[]`），那么运行主程序生成的PV表是无遗漏的

### 输出

- 支持的输出格式为cmd/terminal窗口输出，`txt`文件，`md`文件（方便在线预览）和`xsl`文件（输出`xsl`文件 **默认关闭**）

- 请在此文件末尾指定您需要的输出格式，方法为注释掉不需要的输出方式，或删除需要的输出方式之前的`#`

- 如需要输出`xsl`格式，请安装python的[xlwt库](https://pypi.python.org/pypi/xlwt)（支持写`xsl`文件），删除 `#from xlwt import Workbook` 中的`#`,并在主程序的最下方删除`#pv_out_xls()`中的`#`

- 输出格式为 `[兵种名称] [id]    [PV值]`，使用`Tab`分隔

**示例**

    步兵  s_trooper   4   5   7   9   11  14

    冲击步兵    s_shock 5   7   8   10  11  13


## Battle nations Wiki生成器

>自动生成[Battle Nations Wiki](http://battlenations.wikia.com/wiki/Battle_Nations_Wiki)的工具

仍处于试验阶段，部分功能未完成

有兴趣的可以去`wikia_gen`文件夹下打开`all.py`并将`unit_name = 's_arctic_trooper'`中单引号部分换成想要生成wiki的单位id，在python中运行`python all.py`即可

attack自动生成部分还没做
