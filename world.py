# world.py

class Room:
    # 初始化房间类，包含房间ID、所属城镇ID、名称、描述和出口信息
    def __init__(self, room_id, town_id, room_name, room_description, direction_e, direction_s, direction_w, direction_n):
        self.room_id = room_id
        self.town_id = town_id
        self.name = room_name
        self.description = room_description
        # 存储出口信息的字典
        self.exits = {
            'north': direction_n,
            'east': direction_e,
            'south': direction_s,
            'west': direction_w
        }

    # 根据方向获取出口房间ID，如果方向不存在则返回None
    def get_exit(self, direction):
        # 获取指定方向的出口房间ID
        exit_room_id = self.exits.get(direction, None)
        # 如果房间ID为0，则表示没有出口，返回None
        # 否则返回房间ID
        return None if exit_room_id == '0' else exit_room_id


class Town:
    # 初始化城镇类，包含城镇ID、名称、描述和一个房间列表
    def __init__(self, town_id, name, description):
        self.town_id = town_id
        self.name = name
        self.description = description
        self.rooms = []

    # 向城镇中添加一个房间
    def add_room(self, room):
        self.rooms.append(room)


class World:
    def __init__(self, db):
        self.towns = []
        self.db = db  # 添加数据库连接对象

    def load_towns(self):
        # 从数据库加载所有城镇信息
        cursor = self.db.cursor
        cursor.execute("SELECT * FROM towns")
        towns_data = cursor.fetchall()
        for town_data in towns_data:
            town = Town(*town_data)
            self.towns.append(town)

    def load_rooms(self):
        cursor = self.db.cursor
        cursor.execute("SELECT * FROM rooms")
        rooms_data = cursor.fetchall()
        for room_data in rooms_data:
            room = Room(*room_data)
           # print(f"Loaded room: {room.name} with ID: {room.room_id}")  # 调试信息
            for town in self.towns:
                if town.town_id == room.town_id:
                    town.add_room(room)
                    break

    def get_room(self, room_id):
      #  print(f"Searching for room with ID: {room_id}")
        # 根据房间ID获取房间对象
        for town in self.towns:
            for room in town.rooms:
                if room.room_id == room_id:
                  # print(f"Room found: {room.name}")
                    return room
       # print("No room found with the given ID.")
        return None