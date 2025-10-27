import codecs

from Inputs.Reader import Reader

name: str = "input08.1.txt"
digital_copy = Reader(name).read_txt_to_str()
digital_copy = digital_copy.split("\n")

str_code_length: int = 0
str_memory_length: int = 0

for line in digital_copy:
    str_code_length += len(line)
    escape = codecs.decode(line, "unicode_escape")
    str_memory_length += len(escape)-2

print(str_code_length - str_memory_length)
