# MUD.py
from database import Database
import character
from world import World
from colorama import init, Fore, Back, Style

# 初始化colorama
init(autoreset=True)

# 定义一些颜色常量，方便使用
RED = Fore.RED
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
RESET = Style.RESET_ALL


class PlayerAlreadyExists(Exception):
    pass

class CommandHandler:
    def __init__(self, player_character, game_world):
        self.player_character = player_character
        self.game_world = game_world

    def parse_command(self, command):
        command_parts = command.split(maxsplit=1)  # 使用 maxsplit=1 来正确处理带参数的命令
        action = command_parts[0].lower()

        if action == "look":
            self.handle_look()
        elif action == "go" and len(command_parts) > 1:  # 检查是否有足够的参数
            direction = command_parts[1].lower()
            self.handle_go(direction)
        elif action == "map":
            self.handle_map()
        elif action == "info":
            self.handle_info()
            self.handle_bag()
        elif action == "bag":
            self.handle_bag()
        elif action == "help":
            self.handle_help()
        elif action == "quit":
            self.handle_quit()
        else:
            print("未知命令，请输入有效的命令。")

    def handle_look(self):
        current_room = self.game_world.get_room(self.player_character.player_data['current_roomid'])
        if current_room:
            print(f"{GREEN}\n你环顾四周：{RESET}")
            print(current_room.description)
            print(f"{BLUE}\n出口：{RESET}")
            self.list_exits(current_room)

    def list_exits(self, room):
        for direction in ["north", "east", "south", "west"]:
            exit_room_id = room.get_exit(direction)
            if exit_room_id:
                exit_room = self.game_world.get_room(exit_room_id)
                print(f"{YELLOW}{direction.capitalize()}: {exit_room.name}{RESET}")
            else:
                print(f"{RED}{direction.capitalize()}: 没有出口{RESET}")

    def handle_bag(self):
        # 显示玩家的背包
        bag = self.player_character.get_bag()
        if bag:
            print("背包中有：")
            for item in bag:
                print(f"  {item['name']} - {item['description']} (数量: {item['quantity']})")
        else:
            print("你的背包是空的。\n")
        print("----------------------------")

    def handle_go(self, direction):
        current_room = self.game_world.get_room(self.player_character.player_data['current_roomid'])
        if current_room:
            exit_room_id = current_room.get_exit(direction)
            if exit_room_id:
                exit_room = self.game_world.get_room(exit_room_id)
                if exit_room:
                    self.player_character.player_data['current_roomid'] = exit_room_id
                    print(f"\n你来到了 {RED}{exit_room.name}{RESET}.")
                    print(exit_room.description)
                else:
                    print("尝试进入的房间不存在，请重新输入命令。")
            else:
                print(f"无法前往 {direction.capitalize()} 方向，该方向没有出口。")

    def handle_map(self):
        # 调用 map 模块的 display 方法
        game_map.display()

    def handle_info(self):
        self.player_character.display_info()

    def handle_help(self):
        print("可用命令：")
        print("  look - 查看当前房间描述和出口")
        print("  go [direction] - 向指定方向移动")
        print("  map - 查看地图")
        print("  info - 显示玩家信息")
        print("  bag - 显示玩家背包信息")
        print("  quit - 退出游戏")
        print("  help - 显示帮助信息")

    def list_exits(self, room):
        for direction in ["north", "east", "south", "west"]:
            exit_room_id = room.get_exit(direction)
            if exit_room_id:
                exit_room = self.game_world.get_room(exit_room_id)
                print(f"{direction.capitalize()}: {exit_room.name}")
           

    

    def handle_quit(self):
        print("感谢您参加游戏，再见！")
        exit()

    def handle_rest(self):
        # ... rest 命令逻辑 ...
        pass

    def execute(self, command, *args):
        self.commands[command](*args)

def load_player(db, player_name):
    cursor = db.cursor  # 这里应该使用 db.cursor
    cursor.execute('SELECT * FROM player WHERE name = ?', (player_name,))
    row = cursor.fetchone()
    if not row:
        raise PlayerAlreadyExists("玩家不存在，请创建新角色。")
    return {
        'id': row[0],
        'name': row[1],
        'current_townid': row[2],
        'current_roomid': row[3],
        'health': row[4],
        'inner_power': row[5],
        'attack': row[6],
        'defense': row[7],
        'stamina': row[8]
    }

def create_character():
    # ... 创建角色逻辑 ...
    pass

def main():
    db = Database()
    db.create_tables()

    player_name = input("请输入玩家名称： ")

    try:
        player_character_data = load_player(db, player_name)
        print(f"欢迎回来，{player_name}!\n可以输入help来了解游戏,输入look来查看四周环境。\n")
    except PlayerAlreadyExists as e:
        print(e)
        player_character_data = create_character()
        db.insert_player(
            name=player_character_data['name'],
            current_town=player_character_data['current_townid'],
            current_room=player_character_data['current_roomid'],
            health=player_character_data['health'],
            inner_power=player_character_data['inner_power'],
            attack=player_character_data['attack'],
            defense=player_character_data['defense'],
            stamina=player_character_data['stamina']
        )

    player_character = character.Character(player_character_data, db)
    game_world = World(db)
    game_world.load_towns()
    game_world.load_rooms()
    command_handler = CommandHandler(player_character, game_world)
    # 游戏主循环
    try:
        while True:
            command = input("请输入命令： ").lower()
            command_handler.parse_command(command)
    except Exception as e:
        print(f"{RED}发生错误：{RESET}{e}")
        print("游戏结束。")

if __name__ == "__main__":
    main()