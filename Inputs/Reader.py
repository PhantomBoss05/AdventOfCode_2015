import os

class Reader:
    def __init__(self, file):
        self.file = file
    def read_txt_to_str(self) -> str:
        file = os.path.join(os.path.dirname(os.path.realpath(__file__)), self.file)
        with open(file, 'r', encoding='utf-8') as f:
            return f.read()

    def read_txt_to_list(self) -> list:
        file = os.path.join(os.path.dirname(os.path.realpath(__file__)), self.file)
        with open(file, 'r', encoding='utf-8') as f:
            return f.readlines()




