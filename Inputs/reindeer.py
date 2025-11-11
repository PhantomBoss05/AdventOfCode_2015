

class Reindeer:
    def __init__(self):
        self.name: str = "\0"
        self.speed: int = 0
        self.sleep: int = 0
        self.endurance: int = 0

    def set_speed(self, speed: int):
        self.speed = speed

    def set_sleep(self, sleep: int):
        self.sleep = sleep

    def set_endurance(self, endurance: int):
        self.endurance = endurance

    def set_name(self, name: str):
        self.name = name

    def get_name(self):
        return self.name

    def get_speed(self):
        return self.speed

    def get_sleep(self):
        return self.sleep

    def get_endurance(self):
        return self.endurance