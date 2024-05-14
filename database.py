# database.py

# 导入sqlite3模块，用于操作SQLite数据库
import sqlite3


# 创建Database类，用于数据库操作
class Database:
    def __init__(self):
        # 初始化数据库连接
        self.conn = sqlite3.connect('player_data.db')
        self.cursor = self.conn.cursor()

    def create_tables(self):
        # 如果表不存在，则创建表
        self.cursor.execute(
            'CREATE TABLE IF NOT EXISTS towns ('
            'town_id INTEGER PRIMARY KEY, '
            'town_name TEXT NOT NULL, '
            'town_description TEXT)'
        )

        self.cursor.execute(
            'CREATE TABLE IF NOT EXISTS rooms ('
            'room_id INTEGER PRIMARY KEY, '
            'town_id INTEGER NOT NULL, '
            'room_name TEXT NOT NULL, '
            'room_description TEXT, '
            'direction_e TEXT, '  # 东方向上的房间ID
            'direction_s TEXT, '  # 南方向上的房间ID
            'direction_w TEXT, '  # 西方向上的房间ID
            'direction_n TEXT, '  # 北方向上的房间ID
            'FOREIGN KEY (town_id) REFERENCES towns (town_id))'
        )

        self.cursor.execute(
            'CREATE TABLE IF NOT EXISTS player ('
            'id INTEGER PRIMARY KEY, '
            'name TEXT, '  # 玩家名称
            'current_townid INTEGER, '  # 玩家当前所在城镇id
            'current_roomid INTEGER, '  # 玩家当前所在房间id
            'health INTEGER, '  # 玩家生命值
            'inner_power INTEGER, '  # 玩家内力值
            'attack INTEGER, '  # 玩家攻击力值
            'defense INTEGER, '  # 玩家防御力值
            'stamina INTEGER)'  # 玩家体力值
        )
        self.conn.commit()

    def insert_town(self, town_name, town_description):
        # 插入新的城镇信息到数据库
        self.cursor.execute(
            'INSERT INTO towns (town_name, town_description) VALUES (?, ?)',
            (town_name, town_description)
        )
        self.conn.commit()

    def insert_room(self, town_id, room_name, room_description, direction_e, direction_s, direction_w, direction_n):
        # 插入新的房间信息到数据库
        self.cursor.execute(
            'INSERT INTO rooms (town_id, room_name, room_description, direction_e, direction_s, direction_w, direction_n) VALUES (?, ?, ?, ?, ?, ?, ?)',
            (town_id, room_name, room_description, direction_e, direction_s, direction_w, direction_n)
        )
        self.conn.commit()

    def insert_player(self, name, current_townid, current_roomid, health, inner_power, attack, defense, stamina):
        # 插入新的玩家信息到数据库
        self.cursor.execute(
            'INSERT INTO player (name, current_townid, current_roomid, health, inner_power, attack, defense, stamina) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
            (name, current_townid, current_roomid, health, inner_power, attack, defense, stamina)
        )
        self.conn.commit()

    def update_player_stamina(self, player_id, stamina):
        self.cursor.execute(
            'UPDATE player SET stamina = ? WHERE id = ?',
            (stamina, player_id)
        )
        self.conn.commit()
    def get_town(self, town_id):
        # 通过城镇ID获取城镇信息
        self.cursor.execute('SELECT * FROM towns WHERE town_id = ?', (town_id,))
        return self.cursor.fetchone()

    def get_room(self, room_id):
        # 通过房间ID获取房间信息
        self.cursor.execute('SELECT * FROM rooms WHERE room_id = ?', (room_id,))
        return self.cursor.fetchone()