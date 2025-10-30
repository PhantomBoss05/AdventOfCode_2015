from timeit import default_timer as timer
input_string: str =  "1113122113"
new_verse: str
how_many_times: int = 50
how_many_digits: int = 0
how_many_digits_temp: int = 0
last_digit: str = '\0'
newest_digit: str = '\0'
i: int = 0
last_stop: int = 0

test: int = 1

new_verse = input_string
while how_many_times > 0:
    start = timer()
    last_digit = new_verse[0]

    for digit in new_verse:
        if newest_digit != digit:
            newest_digit = digit

        if digit == last_digit:
            how_many_digits += 1
            last_digit = newest_digit
            
        else:
            new_verse = new_verse[:last_stop] + str(how_many_digits) + last_digit + input_string[i:]
            how_many_digits = 1
            last_digit = newest_digit
            last_stop = last_stop + 2
        i += 1

    new_verse = new_verse[:last_stop] + str(how_many_digits) + last_digit + input_string[i:]
    how_many_digits = 0
    last_digit = newest_digit
    i = 0
    how_many_times -= 1
    last_stop = 0
    input_string = new_verse
    print(50 - how_many_times)
    end = timer()
    print(end - start)
print(len(new_verse)) #360154 | 5103798