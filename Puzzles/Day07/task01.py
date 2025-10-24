from collections import defaultdict

from Inputs.Reader import Reader
from Inputs.bobbys_playground import LogicGate
name: str = "input07.1.txt"

instruction = Reader(name).read_txt_to_str()
instruction = instruction.split("\n")

test: bool  = False
i: int = 0
gates = defaultdict(LogicGate)
wires = {}
print(len(instruction))
for line in instruction:

    line = line.split()

    if line[0].isdigit():
        gates[line[2]].set_data(line[0])
        instruction.pop(i)
    i += 1
print(len(instruction))
i: int = 0
while i < len(instruction):

    line = instruction[i]

    if "AND" in line:
        if line[0].isdigit():
            try:
                gates[line[4]].data = int(line[0]) & gates[line[2]].data
                i += 1
            except TypeError:
                instruction.append(instruction.pop(0))
                #i += -1
                continue
        elif line[2].isdigit():
            try:
                gates[line[4]].data = gates[line[0]].data & int(line[2])
                i += 1
            except TypeError:
                instruction.append(instruction.pop(0))
                #i += -1
                continue
        else:
            try:
                gates[line[4]].data = gates[line[0]].data & gates[line[2]].data
                i += 1
            except TypeError:
                instruction.append(instruction.pop(0))
                #i += -1
                continue

    if "OR" in line:
        if line[0].isdigit():
            try:
                gates[line[4]].data = int(line[0]) | gates[line[2]].data
                i += 1
            except TypeError:
                instruction.append(instruction.pop(0))
                #i += -1
                continue
        elif line[2].isdigit():
            try:
                gates[line[4]].data = gates[line[0]].data | int(line[2])
                i += 1
            except TypeError:
                instruction.append(instruction.pop(0))
                #i += -1
                continue
        else:
            try:
                gates[line[4]].data = gates[line[0]].data | gates[line[2]].data
                i += 1
            except TypeError:
                instruction.append(instruction.pop(0))
                #i += -1
                continue

    if "NOT" in line:
        if line[1].isdigit():
            try:
                gates[line[3]].data = ~int(line[1])
                i += 1
            except TypeError:
                instruction.append(instruction.pop(0))
                #i += -1
                continue
        else:
            try:
                gates[line[3]].data = ~gates[line[1]].data
                i += 1
            except TypeError:
                instruction.append(instruction.pop(0))
                #i += -1
                continue


    if "LSHIFT" in line:
        if line[0].isdigit():
            try:
                gates[line[4]].data = (int(line[0]) << gates[line[2]].data) % 65536
                i += 1
            except TypeError:
                instruction.append(instruction.pop(0))
                #i += -1
                continue
        elif line[2].isdigit():
            try:
                gates[line[4]].data = gates[line[0]].data << int(line[2]) % 65536
                i += 1
            except TypeError:
                instruction.append(instruction.pop(0))
                #i += -1
                continue
        else:
            try:
                gates[line[4]].data = gates[line[0]].data << gates[line[2]].data % 65536
                i += 1
            except TypeError:
                instruction.append(instruction.pop(0))
                #i += -1
                continue

    if "RSHIFT" in line:
        if line[0].isdigit():
            try:
                gates[line[4]].data = int(line[0]) >> gates[line[2]].data
                i += 1
            except TypeError:
                instruction.append(instruction.pop(0))
                #i += -1
                continue
        elif line[2].isdigit():
            try:
                gates[line[4]].data = gates[line[0]].data >> int(line[2])
                i += 1
            except TypeError:
                instruction.append(instruction.pop(0))
                #i += -1
                continue
        else:
            try:
                gates[line[4]].data = gates[line[0]].data >> gates[line[2]].data
                i += 1
            except TypeError:
                instruction.append(instruction.pop(0))
                #i += -1
    else:
        if line[1].isdigit():
            try:
                gates[line[3]].data = int(line[1])
                i += 1
            except TypeError:
                instruction.append(instruction.pop(0))
                #i += -1
                continue
        else:
            try:
                gates[line[3]].data = gates[line[1]].data
                i += 1
            except TypeError:
                instruction.append(instruction.pop(0))
                #i += -1
                continue

print(gates['a'])