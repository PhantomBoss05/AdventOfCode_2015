from Inputs.Reader import Reader
from Inputs.cities import City, CityDistance
from collections import defaultdict
from collections import deque

name: str = "input09.1.txt"
distance_map = Reader(name).read_txt_to_str()
distance_map = distance_map.split("\n")

num_cities: int = 0
name_distance: str
all_cities: deque[str]  = deque()
all_distance: deque[int] = deque()
temp_name: str = '\0'
temp: int = 0
new_key: str = '\0'
past_city: str = '\0'
i: int = 0
shortest_distance: int = 0
route: int = 0

cities = defaultdict(City)
distance = defaultdict(CityDistance)

for line in distance_map:
    if temp_name != line.partition(' ')[0]:
        cities[i].set_city_name(line.partition(' ')[0])
        temp_name = line.partition(' ')[0]
        i += 1
cities[i].set_city_name(distance_map[len(distance_map)-1].partition(' ')[2].partition(' ')[2].partition(' ')[0]) #gives me the last city
num_cities = len(cities)

for key in cities:
    all_cities.append(cities[key].name)

for line in distance_map:
    name_distance: str = line.partition(' ')[0] + '|' + line.partition(' ')[2].partition(' ')[2].partition(' ')[0]
    distance[name_distance].set_fom_city(line.partition(' ')[0])
    distance[name_distance].set_to_city(line.partition(' ')[2].partition(' ')[2].partition(' ')[0])
    distance[name_distance].set_distance(int(line.split(' ')[-1]))

i = 1

for city in all_cities:
    if f"{all_cities[0]}|{city}" in distance:
        all_distance.append(distance[f"{all_cities[0]}|{city}"].distance)
    else:
        continue
shortest_distance = min(all_distance)
all_distance.clear()

while len(all_cities) > 1:
    for key in distance:
        if shortest_distance == distance[key].distance:
            route += shortest_distance
            if new_key != key.split('|')[1]:
                new_key = key.split('|')[1]
                past_city = key.split('|')[0]
            else:
                new_key = key.split('|')[0]
                past_city = key.split('|')[1]
            all_cities.remove(past_city)
            for city in all_cities:
                if f"{new_key}|{city}" in distance:
                    all_distance.append(distance[f"{new_key}|{city}"].distance)
                elif f"{city}|{new_key}" in distance:
                    all_distance.append(distance[f"{city}|{new_key}"].distance)
            if len(all_distance) > 1:
                shortest_distance = min(all_distance)
            elif len(all_distance) == 0:
                break
            else:
                shortest_distance = all_distance[0]
            all_distance.clear()

print(route) #173 too high | 141 richtig
