from Inputs.Reader import Reader
import numpy as np

name: str = "input18.1.txt"
light_instructions = Reader(name).read_txt_to_str()
light_instructions = light_instructions.split('\n')

y: int = 0
x: int = 0
steps: int = 100
animation: bool = False

array_range: int = int(input("Array range [x * x]: "))

lightmap = np.zeros((array_range, array_range), dtype=int)
new_lightmap = np.zeros((array_range, array_range), dtype=int)

for line in light_instructions:
    for light in line:
        match light:
            case"#":
                lightmap[y][x] = 1

                if x < array_range-1:
                    x += 1
                else:
                    y += 1
                    x = 0
            case ".":
                if x < array_range-1:
                    x += 1
                else:
                    y += 1
                    x = 0
def check_line_1_3(i, copy_cy, copy_cx, copy_count_on) -> int:
    while i < 3:
        if (0 > copy_cy or copy_cy >= array_range) or (0 > copy_cx or copy_cx >= array_range):
            copy_cx += 1
            i += 1
            continue
        if lightmap[copy_cy][copy_cx] == 1:
            copy_count_on += 1
        i += 1
        copy_cx += 1
    return copy_count_on

def check_line_2(i, copy_cy, copy_cx, copy_count_on) -> int:
    while i < 3:
        if (0 > copy_cy or copy_cy >= array_range) or (0 > copy_cx or copy_cx >= array_range):
            copy_cx += 1
            i += 1
            continue
        if lightmap[copy_cy][copy_cx] == 1 and i != 1:
            copy_count_on += 1
        i += 1
        copy_cx += 1
    return copy_count_on

def check(copy_x, copy_y, state: int) -> bool:
    count_on: int = 0
    i: int = 0


    copy_y -= 1
    copy_x -= 1
    count_on = check_line_1_3(i, copy_y, copy_x, count_on)

    copy_y += 1
    count_on = check_line_2(i, copy_y, copy_x, count_on)

    copy_y += 1
    count_on = check_line_1_3(i, copy_y, copy_x, count_on)

    if (state == 1 and count_on == 3) or (state == 1 and count_on == 2) or (state == 0 and count_on == 3):
        return True
    return False





for n in range(steps):
    x = 0
    y = 0
    for row in lightmap:
        for light in row:
            match light:
                case 1:
                    animation = check(x, y, 1)
                    if animation:
                        new_lightmap[y][x] = 1
                    else:
                        new_lightmap[y][x] = 0

                    if x < array_range-1:
                        x += 1
                    else:
                        y += 1
                        x = 0
                case 0:
                    animation = check(x, y, 0)
                    if animation:
                        new_lightmap[y][x] = 1
                    else:
                        new_lightmap[y][x] = 0

                    if x < array_range-1:
                        x += 1
                    else:
                        y += 1
                        x = 0
    lightmap = new_lightmap
    new_lightmap = np.zeros((array_range, array_range), dtype=int)


print(np.sum(lightmap)) #821
