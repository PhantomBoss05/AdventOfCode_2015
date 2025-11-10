import re
from Inputs.Reader import Reader
from collections import defaultdict, deque

name: str = "input12.1.txt"
document = Reader(name).read_txt_to_str()
temp_str: str = '\0'
temp_small_str: str = '\0'
i: int = 0
j: int = 0
counter_first: int = 0
counter_second: int = 0
small_counter_first: int = 0
small_counter_second: int = 0

first_cut = defaultdict(int)
second_cut = defaultdict(int)
small_first_cut = defaultdict(int)
small_second_cut = defaultdict(int)

list_counter_first: deque = deque()
list_counter_second: deque = deque()
list_small_counter_first: deque = deque()
list_small_counter_second: deque = deque()

red_in_square: bool = False

for character in document: #Falsch weil red in einem array nicht zählt \{([!-z]*?)\}
    if character == '{':
        first_cut[counter_first] = i
        list_counter_first.append(counter_first)
        counter_first += 1

    if character == '}':
        second_cut[counter_second] = i
        list_counter_second.append(counter_second)
        counter_second += 1
        temp_str = document[first_cut[list_counter_first.pop()]:second_cut[list_counter_second.popleft()]+1]


        if re.findall(r'red', temp_str):
            for sign in temp_str:
                if sign == '[':
                    small_first_cut[small_counter_first] = j
                    list_small_counter_first.append(small_counter_first)
                    small_counter_first += 1

                if sign == ']':
                    small_second_cut[small_counter_second] = j
                    list_small_counter_second.append(small_counter_second)
                    small_counter_second += 1
                    temp_small_str = temp_str[small_first_cut[list_small_counter_first.pop()]:small_second_cut[list_small_counter_second.popleft()]+1]


                    if re.findall(r'red', temp_small_str):
                        temp_str = temp_str.replace(temp_small_str, '')
                        j -= len(temp_small_str)
                        if re.findall(r'red', temp_str):
                            document = document.replace(temp_str, "")
                            i -= len(temp_str)
                        else:
                            red_in_square = True
                j += 1
        if not red_in_square and re.findall(r'red', temp_str):
            document = document.replace(temp_str, "")
            i -= len(temp_str)
        red_in_square = False
    j = 0
    i += 1

numbers = re.findall(r'-?\d+', document)
sum_numbers = sum(map(int, numbers))

print(sum_numbers) #156.366 too high 47.170 too low 154.099 too high

#noch unfertig




