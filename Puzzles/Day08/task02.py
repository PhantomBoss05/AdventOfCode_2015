from Inputs.Reader import Reader

name: str = "input08.1.txt"
digital_copy = Reader(name).read_txt_to_str()
digital_copy = digital_copy.split("\n")
temp: str
str_length: int = 0
str_code_length: int = 0

for line in digital_copy:
    str_code_length += len(line)
    str_length += line.count("\\")*2 #check for \.
    str_length += line.count("\"")*2 #check for "
    str_length += 2 #for the outer "
    str_length += len(line.replace("\"", "").replace("\\", ""))



print(str_length - str_code_length) #7745 | 6545 | 8606 too high