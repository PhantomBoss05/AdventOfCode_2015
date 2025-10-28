from collections import deque, defaultdict


class City:
    def __init__(self):
        self.name: str = '\0'
        self.num_cities: int = 0

    def set_city_name(self, city_name: str):
        self.name = city_name

class CityDistance:
    def __init__(self):
        self.from_city: str = '\0'
        self.to_city: str = '\0'
        self.distance: int | None = None

    def set_fom_city(self, fom_city: str):
        self.from_city = fom_city

    def set_to_city(self, to_city: str):
        self.to_city = to_city

    def set_distance(self, distance: int):
        self.distance = distance

    def get_distance(self):
        return self.distance

def get_route(all_cities: deque, distance: defaultdict) -> int:
    all_distance: int = 0
    last_city: str = '\0'
    i: int = 0
    while i < 8:
        for city in all_cities:
            if f"{last_city}|{city}" in distance:
                all_distance += distance[f"{last_city}|{city}"].distance
                last_city = city
            elif f"{city}|{last_city}" in distance:
                all_distance += distance[f"{city}|{last_city}"].distance
                last_city = city
            else:
                last_city = city
            i += 1
    return all_distance




