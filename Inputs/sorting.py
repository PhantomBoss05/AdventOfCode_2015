from collections import deque

class Stack:
    def __init__(self):
        self.data = deque()

    def add(self, input_data):
        self.data.append(input_data)

    def del_last(self):
        return self.data.pop()

    def del_first(self):
        return self.data.popleft()

    def search_for(self, import_string: list[str], what: str):
        for line in import_string:
            line = line.split(" ")
            if line[1] == "AND" or line[1] == "OR" or line[1] == "LSHIFT" or line[1] == "RSHIFT":
                if line[4] == what:
                    self.data.append(line)
                    break
            elif line[1] == "NOT":
                if line[3] == what:
                    self.data.append(line)
                    break
            elif line[2] == what:
                self.data.append(line)
                break

    @staticmethod
    def search_for_last(import_string: list[str], what: str):
        for line in import_string:
            line = line.split(" ")
            if line[0] == what:
                return line[2]
        return None

    def what_do_i_need(self):
        last: int = len(self.data) -1
        if self.data[last][1] == "AND" or self.data[last][1] == "OR" or self.data[last][1] == "LSHIFT" or self.data[last][1] == "RSHIFT":
            if self.data[last][0].isalpha() and self.data[last][2].isalpha():
                return f"{self.data[last][0]},{self.data[last][2]}"
            elif self.data[last][0].isalpha():
                return self.data[last][0]
            elif self.data[last][2].isalpha():
                return self.data[last][2]
            else:
                raise ValueError("Es wurde keine Variable gefunden (sorting.py)")

        elif self.data[last][0] == "NOT":
            if self.data[last][1].isalpha():
                return self.data[last][0]
            else:
                raise ValueError("Es wurde keine Variable gefunden (NOT sorting.py)")
        else:
            return self.data[last][0]










