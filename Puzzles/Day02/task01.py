from Inputs.Reader import Reader

name: str = "input02.1.txt"
length: int
l: bool = False
width: int
w: bool = False
height: int
h: bool = False
smallest01: int = 0
smallest02: int = 0
qm_sides: list = []

qm: int = 0
wrappingPaper: list[str] = Reader(name).read_txt_to_list()
#print(wrappingPaper)

for line in wrappingPaper:
    lst: list[str] = line.strip().split('x')
    length = int(lst[0])
    width = int(lst[1])
    height = int(lst[2])

    qm_sides = [(length*width),(width*height),(height*length)]

    min_sides = min(qm_sides)
    qm += min_sides + 2*sum(qm_sides)

print(qm)