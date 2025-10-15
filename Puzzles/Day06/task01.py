from Inputs.Reader import Reader
import numpy as np
name: str = "input06.1.txt"
light_instructions = Reader(name).read_txt_to_str()
lights_on: int = 0
santas_list: list[str] = light_instructions.split('\n')
#print(santas_list)

lightmap = np.zeros((1000, 1000), dtype=int)
print(lightmap)
for line in santas_list:
    case = 0 if line.startswith("turn off") else 1 if line.startswith("turn on") else 2
    line = line.replace("turn ", "")
    line = line.split(" ")

    point_one = line[1]
    point_two = line[3]
    point_one = point_one.split(",")
    point_two = point_two.split(",")

    x_one = point_one[0]
    y_one = point_one[1]
    x_two = point_two[0]
    y_two = point_two[1]

    y_start = min(int(y_one), int(y_two))
    y_end = max(int(y_one), int(y_two))
    x_start = min(int(x_one), int(x_two))
    x_end = max(int(x_one), int(x_two))
    if case == 2:
        lightmap[y_start:y_end + 1, x_start:x_end + 1] ^= 1
    else:
        lightmap[y_start:y_end + 1, x_start:x_end + 1] = case




print(lightmap)
lights_on = np.count_nonzero(lightmap == 1)
print(lights_on)