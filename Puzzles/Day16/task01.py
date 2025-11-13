from Inputs.Reader import Reader

name: str = "input16.1.txt"
lst_aunts = Reader(name).read_txt_to_str()
lst_aunts = lst_aunts.split("\n")

key: int = 0
temp_compound: str = "\0"
i: int = 2
points_best_aunt: int = 0
best_aunt: int = 0

class Aunt:
    def __init__(self, memory):
        self.str = memory
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

    def __repr__(self) -> str:
        return f"{self.str}, points: {self.points}"
    def __lt__(self, other):
        return self.points < other.points
    def __gt__(self, other):
        return self.points > other.points
    def __eq__(self, other):
        return self.points == other.points

aunt = []

for line in lst_aunts:
    aunt.append(Aunt(line))
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


def _check(sue: Aunt):
    if sue.children == 3:
        sue.points += 1
    if sue.cats == 7:
        sue.points += 1
    if sue.samoyeds == 2:
        sue.points += 1
    if sue.pomeranians == 3:
        sue.points += 1
    if sue.akitas == 0:
        sue.points += 1
    if sue.vizslas == 0:
        sue.points += 1
    if sue.goldfish == 5:
        sue.points += 1
    if sue.trees == 3:
        sue.points += 1
    if sue.cars == 2:
        sue.points += 1
    if sue.perfumes == 1:
        sue.points += 1
    return sue

print(max(map(_check, aunt)))





