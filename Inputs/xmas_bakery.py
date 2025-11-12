from collections import deque

class Ingredient:
    def __init__(self):
        self.name: str = "\0"
        self.capacity: int = 0
        self.durability: int = 0
        self.flavor: int = 0
        self.texture: int = 0
        self.calories: int = 0