from Reader import Reader
from collections import defaultdict
from reindeer import Reindeer

name: str = "input14.1.txt"
document = Reader(name).read_txt_to_str()
key: int = 0
temp_name: str = "\0"
time: int = 2503
time_fly: int = 0
time_sleep: int = 0
traveled: int = 0

i = defaultdict(int)
j = defaultdict(int)


def run(speed: int, sleep: int, endurance: int, name_reindeer: str, result_race: defaultdict):
    distance: int = 0
    global i
    global j
    if i[name_reindeer] < endurance:
        distance += speed
        i[name_reindeer] += 1
    elif  j[name_reindeer] < sleep:
        j[name_reindeer] += 1
    else:
        distance += speed
        i[name_reindeer] = 1
        j[name_reindeer] = 0

    result_race[name_reindeer] += distance


reindeer = defaultdict(Reindeer)
result = defaultdict(int)
points = defaultdict(int)
document = document.split("\n")

for line in document:
    line = line.split(" ")
    reindeer[key].set_name(line[0])
    reindeer[key].set_speed(int(line[3]))
    reindeer[key].set_endurance(int(line[6]))
    reindeer[key].set_sleep(int(line[13]))

    i[reindeer[key].get_name()] = 0
    j[reindeer[key].get_name()] = 0

    key += 1

while 0 < time:
    for count in range(len(reindeer)):
        run(reindeer[count].get_speed(), reindeer[count].get_sleep(), reindeer[count].get_endurance(), reindeer[count].get_name(), result)
    traveled = max(result.values())

    for data in result:
        if traveled == result[data]:
            points[data] += 1
    time -= 1


print(max(points))          #Vixen
print(max(points.values())) #1059


