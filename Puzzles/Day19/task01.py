from Inputs.Reader import Reader
from re import finditer

name01: str = "input19.1.txt"
name02: str = "input19.2.txt"
replacement = Reader(name01).read_txt_to_str()
replacement = replacement.split('\n')
temp_int: list[int] = []
new_molecule: list[str] = []
unique_molecule: list[str] = []

input_molecule: str = Reader(name02).read_txt_to_str()

for line in replacement:
    line = line.split(" ")
    temp_int = [match.start() for match in finditer(line[0], input_molecule)]
    for match in temp_int:
        new_molecule.append(input_molecule[:match] + line[2] + input_molecule[match + len(line[0]):])

for molecule in new_molecule:
    if molecule not in unique_molecule:
        unique_molecule.append(molecule)

print(unique_molecule)
print(len(unique_molecule))