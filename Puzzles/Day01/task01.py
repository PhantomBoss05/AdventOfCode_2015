from Inputs.Reader import Reader
floor: int = 0
temp: int = 0
length: int
name: str = 'input01.1.txt'
path: str = Reader(name).read_txt_to_str()
length = len(path)

while temp < length:
    if path[temp] == '(':
        floor += 1
    elif path[temp] == ')':
        floor -= 1
    temp += 1

print(floor)
floor = 0

for i in range(length):
    if path[i] == '(':
        floor += 1
    elif path[i] == ')':
        floor -= 1

print(floor)
floor = 0

for c in path:
    if c == '(':
        floor += 1
    elif c == ')':
        floor -= 1
print(floor)

print(sum([-1 if c == ')' else 1 for c in path]))