from sympy import divisors
from collections import defaultdict
_input: int = 34000000
found: bool = False
n: int = 0
temp_divisors: list[int] = []

class House:
    def __init__(self):

        self.presents: int = 0

    def add_present(self, elf_multiplier: int) -> None:
        self.presents += elf_multiplier*10

house= defaultdict(House)
while not found:
    n += 1
    temp_divisors.extend(divisors(n))
    for number in temp_divisors:
        house[n].add_present(number)
        if house[n].presents >= _input:
            found = True
            print(f"Hausnummer: {n}, Geschenke: {house[n].presents}")

    temp_divisors.clear()