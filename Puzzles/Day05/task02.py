from Inputs.Reader import Reader
name: str = "input05.1.txt"
naughty_or_nice = Reader(name).read_txt_to_str()
santas_list: list[str] = naughty_or_nice.split('\n')

character_pair: str ="\0"
counter_nice_strings: int = 0
pair: bool = False
between: bool = False

for letter in santas_list:
    #check for (xyxy) pair
    for i in range(len(letter)-1):
        character_pair = letter[i] + letter[i+1]
        if letter.count(character_pair) >= 2:
            pair = True
    #check for (zxz) between
    for i in range(len(letter)-2):
        if letter[i] == letter[i+2]:
            between = True
    #check if both are true
    if between and pair:
        counter_nice_strings += 1
        print(letter)
    between, pair = False, False


print(counter_nice_strings)



