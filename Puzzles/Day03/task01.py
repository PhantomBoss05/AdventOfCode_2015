from Inputs.Reader import Reader
#from collections import defaultdict
name: str = "input03.1.txt"

way = Reader(name).read_txt_to_str()

x: int = 0
y: int = 0


address: dict [tuple[int, int], int] = {(x, y): 1}
#address: defaultdict = defaultdict(int)
#address[(0, 0)] = 1

for elf in way:
    match elf:
        case ">":
            x += 1
        case "<":
            x += -1
        case "v":
            y += -1
        case "^":
            y += 1



    if (x, y) in address:
        address[(x, y)] += 1

    else:
        address[(x, y)] = 1



print(address)
print(len(address))