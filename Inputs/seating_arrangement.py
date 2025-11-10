from collections import deque

class Member:
    def __init__(self):
        self.name: str = "\0"
        self.happiness_list: deque = deque()

    def set_name(self, name):
        self.name = name

    def add_happiness(self, happiness: int, person: str):
        self.happiness_list.append([person, happiness])

def get_happiness(all_people: deque[Member]) -> int:
    temp_start: str
    happiness = 0
    temp_start = all_people[0].name
    next_person: str
    last_person: str = all_people[-1].name
    i: int = 1

    for people in all_people:
        try:
            next_person = all_people[i].name
            for arrays in people.happiness_list:
                if arrays[0] == next_person or arrays[0] == last_person:
                    happiness += arrays[1]
            last_person = people.name
        except IndexError:
            for arrays in people.happiness_list:
                if arrays[0] == temp_start or arrays[0] == last_person:
                    happiness += arrays[1]

        i += 1

    return happiness


