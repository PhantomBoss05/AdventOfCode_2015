from Inputs.Reader import Reader
from collections import defaultdict
from Inputs.reindeer import Reindeer
from threading import Thread
from tqdm import tqdm
import time as ti

name: str = "input14.1.txt"
document = Reader(name).read_txt_to_str()
key: int = 0
temp_name: str = "\0"

def run(speed: int, sleep: int, endurance: int, name_reindeer: str, result_race: defaultdict):
    time: int = 2503
    distance: int = 0
    i: int = 0
    j: int = 0
    pbar = tqdm(total=time, desc=f"{name_reindeer}\t", position=0, bar_format='{desc}: |{bar}| {percentage:3.0f}%')

    while 0 < time:
        while i < endurance:
            if 0 >= time:
                break
            distance += speed
            time -= 1
            pbar.update(1)
            ti.sleep(0.001)
            i += 1
        i = 0
        while  j < sleep:
            if 0 >= time:
                break
            time -= 1
            pbar.update(1)
            ti.sleep(0.001)
            j += 1
        j = 0

    result_race[name_reindeer] = distance

reindeer = defaultdict(Reindeer)
result = defaultdict(int)
document = document.split("\n")

for line in tqdm(document, desc="Reading", position=0, leave=False, bar_format= '{desc}: |{bar}| {percentage:3.0f}%'):
    line = line.split(" ")
    reindeer[key].set_name(line[0])
    reindeer[key].set_speed(int(line[3]))
    reindeer[key].set_endurance(int(line[6]))
    reindeer[key].set_sleep(int(line[13]))
    key += 1
    ti.sleep(0.1)

threads = []
for n in range(len(reindeer)):
    t = Thread(target=run, args=(reindeer[n].get_speed(), reindeer[n].get_sleep(), reindeer[n].get_endurance(), reindeer[n].get_name(), result))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print(max(result.values())) #2655






