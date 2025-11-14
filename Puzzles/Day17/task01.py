from Inputs.Reader import Reader
from itertools import combinations
from tqdm import tqdm

name: str = "input17.1.txt"
container = Reader(name).read_txt_to_str()
container = container.split("\n")

possibilities: list[tuple[str, ...]] = []
possibilities_int: list[list[int]] = []
valid_combinations: list[list[int]] = []
temp_list: list[int] = []

for i in range(1, len(container)):
    for combination in combinations(container, i):
        possibilities.append(combination)
    i += 1

for line in tqdm(possibilities, desc="str -> int", position=0, leave=False, bar_format= '{desc}: |{bar}| {percentage:3.0f}%'):                              #convert from tuple[str] to list[int]
    for digit in line:
        temp_list.append(int(digit))
    possibilities_int.append(temp_list)
    temp_list = []

for combination in possibilities_int:
    if sum(combination) == 150:
        valid_combinations.append(combination)

print(len(valid_combinations)) #4372

