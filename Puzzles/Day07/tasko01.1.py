from sorting import Stack
from Inputs.Reader import Reader
from bobbys_playground import LogicGate
from collections import defaultdict

name: str = "input07.1.txt"
name_gate: str = "\0"
instruction = Reader(name).read_txt_to_str()
instruction = instruction.split("\n")

gates = defaultdict(LogicGate)

temp: str = 'a'                                                                                                         #das gesuchte gate
temp2: str = '\0'                                                                                                       #zwischenspeicher um zu checken, ob es das darauf folgende gate schon gibt
temp3: str = '\0'                                                                                                       #zwischenspeicher um temp 2 nicht zerschneiden zu müssen
next_search = Stack()                                                                                                   #speicher für alle übersprungenen gates (x and y -> z) y = next search x = temp und z das nächste temp

stack = Stack()                                                                                                         #speichert den weg (assembly Anweisungen)

while not temp.isdigit():
    stack.search_for(instruction, temp)                                                                                 #sucht das geforderte gate 'a' = lx -> a

    print(stack.data)

    temp = stack.what_do_i_need() #lw,lv                                                                                #schaut was für a gebraucht wird (lx)
    if len(temp) > 2 and not temp.isdigit():                                                                            #sollten in temp 2 Zeichen sein z.B. lw, lv wird lv in next_search gelegt und mit lw weitergemacht
        temp = temp.split(",")
        next_search.add(temp[1])
        temp = str(temp[0])
        print(temp)
    else:
        print(temp)

name_gate = stack.search_for_last(instruction, temp)                                                                    #wenn ein Zeichen auf eine einzelne Zahl stößt wird ein gate für dieses Zeichen angelegt (0 -> c) Gatename: c Gatedaten: 0
gates[name_gate] = LogicGate()
gates[name_gate].set_data(temp)
gates[name_gate].set_name(name_gate)

temp = next_search.del_last()

while next_search:                                                                                                      #wiederhohlt die erste while schleife bis next_search leer ist
    while not temp.isdigit():
        stack.search_for(instruction, temp)

        print(stack.data)

        temp2 = stack.what_do_i_need()

        if len(temp2) > 2 and not temp2.isdigit():                                                                      #['d', 'OR', 'j', '->', 'k'], ['b', 'RSHIFT', '2', '->', 'd'] b kenne ich schon, ich muss also nicht mehr danach suchen. Was, wenn statt zwei dort z.B. z stünde. Dann müsste ich dieses noch suchen !!! Fehler fixen
            temp3 = temp2.split(",")
            if gates.__contains__(temp3[0]) or gates.__contains__(temp3[1]):
                gates[temp] = LogicGate()
                gates[temp].set_name(temp)
                break
            else:
                temp = temp2
        elif gates.__contains__(temp2):
            gates[temp] = LogicGate()
            gates[temp].set_name(temp)
            break
        else:
            temp = temp2

        if len(temp) > 2 and not temp.isdigit():
            temp = temp.split(",")
            if not gates.__contains__(temp[1]):
                next_search.add(temp[1])                                                                                #packt das übrig gebliebene Zeichen in next_search sollte es das gate noch nicht geben
            temp = str(temp[0])
            print(temp)
        else:
            print(temp)
    if not gates.__contains__(temp):                                                                                    #erstellt ein gate sollte es noch keines geben und wie b 0 -> c kein weiteres Zeichen das sein
        name_gate = stack.search_for_last(instruction, temp)
        gates[name_gate] = LogicGate()
        gates[name_gate].set_data(temp)
        gates[name_gate].set_name(name_gate)

    print(gates)                                                                                                        #debugging
    print(len(next_search.data))
    temp = next_search.del_last()
    print(len(gates))








