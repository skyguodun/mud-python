
# character.py

class Character:
    def __init__(self, player_data, db):
        self.player_data = player_data
        self.db = db  # 添加db作为Character类的属性

    def display_info(self):
        player_data = self.player_data
        current_town_name = self.db.get_town(player_data['current_townid'])[1]
        current_room_name = self.db.get_room(player_data['current_roomid'])[2]

        print(f"当前【城镇】-【位置】: {current_town_name}----{current_room_name}")

        print(f"---------------{player_data['id']}--------------------------")

        print(f"【人物】: {player_data['name']} | 【体力】: {player_data['stamina']}")
        print(f"【生命】: {player_data['health']} | 【内力】 {player_data['inner_power']}")
        print(f"【攻击】: {player_data['attack']} | 【防御】: {player_data['defense']}")
       
        print(f"-----------------------------------------")

    def get_bag(self):
        # 获取玩家ID
        player_id=self.player_data['id']

        # 执行数据库查询
        cursor = self.db.cursor
        cursor.execute("""
            SELECT items.name, items.description, player_items.quantity
            FROM player_items
            JOIN items ON player_items.item_id = items.item_id
            WHERE player_items.player_id = ?
        """, (player_id,))

        # 获取查询结果
        rows = cursor.fetchall()

        # 格式化结果
        bag = [{"name": row[0], "description": row[1], "quantity": row[2]} for row in rows]

        return bag