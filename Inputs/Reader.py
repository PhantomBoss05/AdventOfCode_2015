import os
class Reader:
    def __init__(self, path):
        self.path = path

    def read(self) -> str:
        path = os.path.join(os.path.dirname(os.path.realpath(__file__)), self.path)
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()

