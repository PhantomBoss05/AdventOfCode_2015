from Inputs.Reader import Reader

name: str = "input03.1.txt"
way = Reader(name).read_txt_to_str()

x: int = 0
y: int = 0
x_robo: int = 0
y_robo: int = 0

switch_santa: bool = True

address: dict [tuple[int, int], int] = {(x, y): 1}
address_robo: dict [tuple[int, int], int] = {(x_robo, y_robo): 1}

for elf in way:

    if elf == ">" and switch_santa:
        x += 1
    elif elf == "<" and switch_santa:
        x += -1
    elif elf == "v" and switch_santa:
        y += -1
    elif elf == "^" and switch_santa:
        y += 1

    if (x, y) in address and switch_santa:
        address[(x, y)] += 1
    elif switch_santa:
        address[(x, y)] = 1
    if switch_santa:
        switch_santa = False
        continue

    if elf == ">" and not switch_santa:
        x_robo += 1
    elif elf == "<" and not switch_santa:
        x_robo += -1
    elif elf == "v" and not switch_santa:
        y_robo += -1
    elif elf == "^" and not switch_santa:
        y_robo += 1

    if (x_robo, y_robo) in address and not switch_santa:
        address[(x_robo, y_robo)] += 1
    elif not switch_santa:
        address[(x_robo, y_robo)] = 1
    if not switch_santa:
        switch_santa = True

print(address)
print(len(address))