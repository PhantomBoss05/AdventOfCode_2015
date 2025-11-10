from Inputs.Reader import Reader
from Inputs.seating_arrangement import Member, get_happiness
import itertools
from collections import defaultdict, deque

name: str = "input13.2.txt"
happiness_list = Reader(name).read_txt_to_str()

i: int = 0
temp_name: str = "\0"
names: list[Member] = []
all_people: deque[Member]  = deque()
all_happiness: list[int] = []


people = defaultdict(Member)

happiness_list = happiness_list.replace("gain ", "")
happiness_list = happiness_list.replace("lose ", "-")
happiness_list = happiness_list.replace(".", "")
happiness_list = happiness_list.split("\n")

for line in happiness_list:
    if temp_name != line.partition(' ')[0]:
        people[i].set_name(line.partition(' ')[0])
        temp_name = line.partition(' ')[0]
        i += 1
    line = line.split(" ")
    people[i-1].add_happiness(int(line[2]), line[9])

for key in people:
    names.append(people[key])

for perm in itertools.permutations(names):
    all_people.extend(perm)
    all_happiness.append(get_happiness(all_people)) #happiness berechnen
    all_people.clear()

print(max(all_happiness)) #733 without me, 725 with me