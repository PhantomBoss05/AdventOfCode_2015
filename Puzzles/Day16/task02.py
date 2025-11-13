from Inputs.Reader import Reader
from collections import defaultdict, deque

name: str = "input16.1.txt"
lst_aunts = Reader(name).read_txt_to_str()
lst_aunts = lst_aunts.split("\n")

key: int = 0
temp_compound: str = "\0"
i: int = 2
points_best_aunt: int = 0
best_aunt: int = 0

class Aunt:
    def __init__(self):
        self.children: int | None = None
        self.cats: int | None = None
        self.samoyeds: int | None = None
        self.pomeranians: int | None = None
        self.akitas: int | None = None
        self.vizslas: int | None = None
        self.goldfish: int | None = None
        self.trees: int | None = None
        self.cars: int | None = None
        self.perfumes: int | None = None
        self.points: int = 0

aunt = defaultdict(Aunt)

for line in lst_aunts:
    line = line.replace(",", "")
    line = line.replace(":", "")
    line = line.split(" ")

    while i <= 6:
        temp_compound = line[i]

        match temp_compound:
            case "children":
                aunt[key].children = int(line[i+1])
            case "cats":
                aunt[key].cats = int(line[i+1])
            case "samoyeds":
                aunt[key].samoyeds = int(line[i+1])
            case "pomeranians":
                aunt[key].pomeranians = int(line[i+1])
            case "akitas":
                aunt[key].akitas = int(line[i+1])
            case "vizslas":
                aunt[key].vizslas = int(line[i+1])
            case "goldfish":
                aunt[key].goldfish = int(line[i+1])
            case "trees":
                aunt[key].trees = int(line[i+1])
            case "cars":
                aunt[key].cars = int(line[i+1])
            case "perfumes":
                aunt[key].perfumes = int(line[i+1])
        i += 2
    i = 2
    key += 1

for key in aunt:
    if aunt[key].children == 3:
        aunt[key].points += 1
    try:
        if aunt[key].cats > 7:
            aunt[key].points += 1
    except TypeError:
        pass
    if aunt[key].samoyeds == 2:
        aunt[key].points += 1
    try:
        if aunt[key].pomeranians < 3:
            aunt[key].points += 1
    except TypeError:
        pass
    if aunt[key].akitas == 0:
        aunt[key].points += 1
    if aunt[key].vizslas == 0:
        aunt[key].points += 1
    try:
        if aunt[key].goldfish < 5:
            aunt[key].points += 1
    except TypeError:
        pass
    try:
        if aunt[key].trees > 3:
            aunt[key].points += 1
    except TypeError:
        pass
    if aunt[key].cars == 2:
        aunt[key].points += 1
    if aunt[key].perfumes == 1:
        aunt[key].points += 1

for key in aunt:
    if aunt[key].points > points_best_aunt:
        points_best_aunt = aunt[key].points
        best_aunt = key+1

print(best_aunt) #260





