from Inputs.Reader import Reader
name: str = "input05.1.txt"
naughty_or_nice = Reader(name).read_txt_to_str()
counter_nice_strings: int = 0

counter_vowels: int = 0
twice_letter:bool = False
santas_list: list[str] = naughty_or_nice.split('\n')


for letter in santas_list:
    twice_letter = False
    for i in range(len(letter)-1):
        if letter[i] == letter[i+1]:
            twice_letter = True
    counter_vowels = letter.count('a') + letter.count('e') + letter.count('i') + letter.count('o') + letter.count('u')
    if counter_vowels < 3 or not twice_letter:
        continue
    if letter.count("ab") < 1 and letter.count("cd") < 1 and letter.count("pq") < 1 and letter.count("xy") < 1:
        counter_nice_strings += 1

print(counter_nice_strings)





