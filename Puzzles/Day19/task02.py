from Inputs.Reader import Reader
from re import finditer
from queue import Queue
from threading import Thread, Event, Lock

name01: str = "input19.1.txt"
name02: str = "input19.2.txt"
replacement = Reader(name01).read_txt_to_str()
replacement = replacement.split('\n')
new_molecule: list[str] = []
unique_molecule: list[str] = []

input_molecule: str = Reader(name02).read_txt_to_str()

q = Queue()
done = Event()
lock = Lock()

def replace(_replacement: str, _input_molecule: str):
    for line in _replacement:
        line = line.split(" ")
        temp_int = [match.start() for match in finditer(line[0], _input_molecule)]
        for match in temp_int:
            new_molecule.append(_input_molecule[:match] + line[2] + _input_molecule[match + len(line[0]):])


num_threads = 8
threads = [Thread(target=worker, daemon=True) for _ in range(num_threads)]
for t in threads:
    t.start()
q.put((input_molecule, 0))
done.wait()
