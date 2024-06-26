# mud-python
这是一个通过python 开发的一个单机版的MUD游戏(开发版的草稿版) 。
# MUD Game
一个基于文本的多人地下城游戏（MUD），使用Python开发。
## 简介
MUD游戏是一种古老而经典的游戏形式，玩家通过文本命令在虚拟世界中探索、战斗和解谜。本项目旨在提供一个简单的MUD游戏框架，玩家可以创建角色、探索城镇和房间、查看周围环境等。
## 安装
1. 确保你的计算机上安装了Python 3。
2. 克隆或下载此项目到本地。
3. 在项目根目录下运行`pip install -r requirements.txt`安装所需的依赖。

## 运行游戏
在项目根目录下运行`python mud.py`即可开始游戏。

## 代码结构
以下是项目的代码结构概览：

lua

├── database.py          # 数据库操作类

├── character.py         # 玩家角色类

├── world.py             # 游戏世界类，包含城镇和房间

├── map.py               # 地图显示类

├── mud.py               # 主游戏循环和命令处理

└── requirements.txt    # 项目依赖
每个文件的具体功能如下：

- `database.py`：负责创建和操作SQLite数据库，存储城镇、房间和玩家信息。
- `character.py`：定义玩家角色类，包含玩家的属性和背包信息。
- `world.py`：定义游戏世界，包括城镇和房间的组织结构。
- `map.py`：负责显示游戏的地图信息。
- `mud.py`：游戏的主入口，包含命令解析和游戏循环。

## 游戏玩法
玩家通过输入命令与游戏互动。以下是一些基本命令：
- `look`：查看当前房间的描述和可用出口。
- `go [direction]`：向指定方向移动。
- `map`：查看当前游戏世界的地图。
- `info`：显示玩家的基本信息。
- `bag`：查看玩家背包中的物品。
- `help`：显示可用命令列表。
- `quit`：退出游戏。

## 贡献
欢迎对本项目做出贡献。如果你有任何改进建议或发现了bug，请通过GitHub Issues或Pull Requests提交。

## 许可证
本项目采用[MIT License](LICENSE)。

## 作者
- skyguodun - 
