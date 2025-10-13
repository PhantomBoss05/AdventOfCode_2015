from Inputs.Reader import Reader

name: str = "input02.1.txt"
length: int
width: int
height: int
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