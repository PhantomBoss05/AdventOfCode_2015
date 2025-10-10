from Inputs.Reader import Reader
floor: int = 0
length: int
name: str = 'input01.1.txt'
path: str = Reader(name).read_txt_to_str()
length = len(path)

for i in range(length):
    if path[i] == '(':
        floor += 1
    elif path[i] == ')':
        floor -= 1
    if floor == -1:
        break

print("Santa enters the basement [", floor, "] on turn", i+1)