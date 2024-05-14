
# map.py

class Map:
    def __init__(self, game_world):
        self.game_world = game_world

    def display(self):
        # This method will be responsible for displaying the map.
        for town in self.game_world.towns:
            print(f"城镇: {town.name}")
            for room in town.rooms:
                print(f"  - {room.name}: {room.description}")
