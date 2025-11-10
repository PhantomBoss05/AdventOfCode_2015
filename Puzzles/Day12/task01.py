import re
from Inputs.Reader import Reader

name: str = "input12.1.txt"
document = Reader(name).read_txt_to_str()

numbers = re.findall(r'-?\d+', document)
sum_numbers = sum(map(int, numbers))

print(sum_numbers)
