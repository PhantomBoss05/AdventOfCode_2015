from collections import deque, defaultdict

old_password: deque[str] = deque(['h','x','b','x','x','y','z','z'])
new_password: deque[str] = deque()
str_password: str = '\0'
len_password: int = 8
character_dez: int
character_symbol: str
#alphabet: deque[str] = deque(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
check: bool = False
is_character_z: bool = False
incrementing: bool = False
check_new_character: bool = False
count: int = 0
temp1: str = '\0'

two_twins: int = 0
increasing_straight: bool = False

temp = defaultdict(int)

while not check:

    while old_password:
        character_symbol = old_password.pop()
        character_dez = ord(character_symbol)

        if character_dez >= 122 and not check_new_character and not incrementing:
            is_character_z = True
        elif incrementing:
            new_password.appendleft(character_symbol)
            continue
        elif check_new_character:
            if ord(character_symbol) > 122:
                is_character_z = True
            else:
                is_character_z = False
                incrementing = True
                check_new_character = False
                new_password.appendleft(character_symbol)
                continue
        else:
            is_character_z = False

        match is_character_z:
            case True:
                new_password.appendleft('a')
                character_symbol = old_password.pop()
                character_dez = ord(character_symbol)
                character_dez = character_dez +1
                old_password.append(chr(character_dez))
                check_new_character = True

            case False:
                character_dez += 1
                new_password.appendleft(chr(character_dez))
                incrementing = True

    incrementing = False
    old_password = deque(new_password)
    count = 0

    for i in new_password:

        #check for i, o, l
        if i == 'i' or i == 'o' or i == 'l':
            break

        #check for two twin characters
        if i == temp1:
            two_twins += 1
            temp1 = '\0'
        else:
            temp1 = i

        #check for increasing straight characters
        temp[count] = ord(i)

        try:
            if temp[count] == temp[count-1]+1 and temp[count] == temp[count-2]+2:
               increasing_straight = True
        except IndexError:
            continue

        count += 1
    temp1 = '\0'
    if increasing_straight and two_twins > 1:
        check = True
        break

    #print(old_password)
    new_password.clear()
    two_twins = 0
    increasing_straight = False


print(new_password) #hxcaabcc








