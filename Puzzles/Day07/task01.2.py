from Inputs.Reader import Reader
from bobbys_playground import LogicGate
from bobbys_playground import Wire
from collections import defaultdict, deque

name: str = "input07.1.txt"
name_gate: str = "\0"
name_wire: str = "\0"
instruction = Reader(name).read_txt_to_str()
instruction = instruction.split("\n")

gates = defaultdict(LogicGate)
wires = defaultdict(Wire)

i: int = 0

for line in instruction:
    line = line.split(" ")
    name_gate = line[len(line) - 1]
    gates[name_gate] = LogicGate()
    gates[name_gate].set_name(name_gate)
    print(gates[name_gate].name, gates[name_gate])

print(len(gates))

for line in instruction:
    line = line.split(" ")

    match len(line):
        case 5:     #kg OR kf -> kh
            if line[0].isdigit():
                name_wire = line[0] + line[1] + line[2]
                wires[name_wire] = Wire()
                wires[name_wire].set_logic_calculation(line[1])
                wires[name_wire].set_destination(gates[line[4]])
                wires[name_wire].set_logic_input([str([line[0]]), gates[line[2]]])
            elif line[2].isdigit():
                name_wire = line[0] + line[1] + line[2]
                wires[name_wire] = Wire()
                wires[name_wire].set_logic_calculation(line[1])
                wires[name_wire].set_destination(gates[line[4]])
                wires[name_wire].set_logic_input([gates[line[0]], str([line[2]])])
            else:
                name_wire = line[0] + line[1] + line[2]
                wires[name_wire] = Wire()
                wires[name_wire].set_logic_calculation(line[1])
                wires[name_wire].set_destination(gates[line[4]])
                wires[name_wire].set_logic_input([gates[line[0]], gates[line[2]]])
            print(wires[name_wire].logic_input, wires[name_wire].logic_calculation, wires[name_wire].destination)
        case 4:     #NOT gs -> gt
            if line[0].isdigit():
                name_wire = line[0] + line[1]
                wires[name_wire] = Wire()
                wires[name_wire].set_logic_calculation(line[0])
                wires[name_wire].set_destination(gates[line[3]])
                wires[name_wire].set_logic_input([str([line[1]]), [line[1]]])
            else:
                name_wire = line[0] + line[1]
                wires[name_wire] = Wire()
                wires[name_wire].set_logic_calculation(line[0])
                wires[name_wire].set_destination(gates[line[3]])
                wires[name_wire].set_logic_input([gates[line[1]], gates[line[1]]])
            print(wires[name_wire].logic_input, wires[name_wire].logic_calculation, wires[name_wire].destination)
        case 3:     #44430 -> b
            if line[0].isdigit():
                gates[line[2]].set_data(int(line[0]))
                print(gates[name_gate].name, gates[name_gate])
            else:
                name_wire = line[0] + 'IS' + line[2]
                wires[name_wire] = Wire()
                wires[name_wire].set_logic_calculation("IS")
                wires[name_wire].set_destination(gates[line[2]])
                wires[name_wire].set_logic_input([gates[line[0]], gates[line[0]]])
                print(wires[name_wire].logic_input, wires[name_wire].logic_calculation, wires[name_wire].destination)

queue = deque(wires.keys())

while queue:
    key = queue.popleft()
    wire = wires[key]

    if wire.is_ready():
        match wire.logic_calculation:
            case "AND":     #eg AND ei -> ej
                if wire.logic_input[0].isdigit():
                    gates[wire.destination].set_data(int(wire.logic_input[0]) & gates[wire.logic_input[1]].data)
                elif wire.logic_input[1].isdigit():
                    gates[wire.destination].set_data(gates[wire.logic_input[0]].data & int(wire.logic_input[1]))
                else:
                    gates[wire.destination].set_data(gates[wire.logic_input[0]].data & gates[wire.logic_input[1]].data)
            case "OR":      #kg OR kf -> kh
                if wire.logic_input[0].isdigit():
                    gates[wire.destination].set_data(int(wire.logic_input[0]) | gates[wire.logic_input[1]].data)
                elif wire.logic_input[1].isdigit():
                    gates[wire.destination].set_data(gates[wire.logic_input[0]].data | int(wire.logic_input[1]))
                else:
                    gates[wire.destination].set_data(gates[wire.logic_input[0]].data | gates[wire.logic_input[1]].data)
            case "NOT":     #NOT dq -> dr
                if wire.logic_input[0].isdigit():
                    gates[wire.destination].set_data(~int(wire.logic_input[0]))
                else:
                    gates[wire.destination].set_data(~gates[wire.logic_input[0]].data)
            case "IS":      #44430 -> b
                if wire.logic_input[0].isdigit():
                    gates[wire.destination].set_data(int(wire.logic_input[0]))
                else:
                    gates[wire.destination].set_data(gates[wire.logic_input[0]].data)
            case "LSHIFT":  #eo LSHIFT 15 -> es
                if wire.logic_input[0].isdigit():
                    gates[wire.destination].set_data((int(wire.logic_input[0]) << gates[wire.logic_input[1]].data) % 65536)
                elif wire.logic_input[1].isdigit():
                    gates[wire.destination].set_data((gates[wire.logic_input[0]].data << int(wire.logic_input[1])) % 65536)
                else:
                    gates[wire.destination].set_data((gates[wire.logic_input[0]].data << gates[wire.logic_input[1]].data) % 65536)
            case "RSHIFT":  #lf RSHIFT 2 -> lg
                if wire.logic_input[0].isdigit():
                    gates[wire.destination].set_data(int(wire.logic_input[0]) >> gates[wire.logic_input[1]].data)
                elif wire.logic_input[1].isdigit():
                    gates[wire.destination].set_data(gates[wire.logic_input[0]].data >> int(wire.logic_input[1]))
                else:
                    gates[wire.destination].set_data(gates[wire.logic_input[0]].data >> gates[wire.logic_input[1]].data)

    else:
        queue.append(key)  # nach hinten schieben
