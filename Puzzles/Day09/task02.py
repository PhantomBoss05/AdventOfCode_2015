from Inputs.Reader import Reader
from Inputs.cities import City, CityDistance, get_route
from collections import defaultdict
from collections import deque
import itertools

name: str = "input09.1.txt"
distance_map = Reader(name).read_txt_to_str()
distance_map = distance_map.split("\n")

cities = defaultdict(City)
distance = defaultdict(CityDistance)

i: int = 0
temp_name: str = '\0'
staedte: list[str] = []
all_cities: deque[str]  = deque()
all_routs: list[int] = []


for line in distance_map:
    if temp_name != line.partition(' ')[0]:
        cities[i].set_city_name(line.partition(' ')[0])
        temp_name = line.partition(' ')[0]
        i += 1
cities[i].set_city_name(distance_map[len(distance_map)-1].partition(' ')[2].partition(' ')[2].partition(' ')[0]) #gives me the last city

for line in distance_map:
    name_distance: str = line.partition(' ')[0] + '|' + line.partition(' ')[2].partition(' ')[2].partition(' ')[0]
    distance[name_distance].set_fom_city(line.partition(' ')[0])
    distance[name_distance].set_to_city(line.partition(' ')[2].partition(' ')[2].partition(' ')[0])
    distance[name_distance].set_distance(int(line.split(' ')[-1]))

for key in cities:
    staedte.append(cities[key].name)

for perm in itertools.permutations(staedte):
    all_cities.extend(perm)
    all_routs.append(get_route(all_cities, distance))
    all_cities.clear()

print(min(all_routs)) #736