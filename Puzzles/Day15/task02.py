from Inputs.Reader import Reader
from collections import defaultdict, deque
import itertools
from xmas_bakery import Ingredient
from tqdm import tqdm

name: str = "input15.1.txt"
kitchen = Reader(name).read_txt_to_str()
kitchen = kitchen.split("\n")
key: int = 0
all_combinations: deque[tuple] = deque()

ingredients = defaultdict(Ingredient)
score:deque[int] = deque()
full_meal_cookies: deque[int] = deque()
temp_score_cap: int = 0
temp_score_du: int = 0
temp_score_fl: int = 0
temp_score_te: int = 0
temp_score_cal: int = 0

def generate_combinations(n, total):
    candidates = range(1, total)
    valid_combinations: deque[tuple] = deque()
    pbar = tqdm(total=96059601, desc= "generate combinations", bar_format='{desc}: |{bar}|{percentage:3.0f}% ({remaining}sec)')

    for combination in itertools.product(candidates, repeat=n):
        pbar.update(1)
        if sum(combination) == total:
            valid_combinations.append(combination)
    return valid_combinations


for line in kitchen:
    line = line.replace(",", "")
    line = line.split(" ")
    ingredients[key].name = line[0]
    ingredients[key].capacity = int(line[2])
    ingredients[key].durability = int(line[4])
    ingredients[key].flavor = int(line[6])
    ingredients[key].texture = int(line[8])
    ingredients[key].calories = int(line[10])
    key += 1

all_combinations = generate_combinations(4, 100)

for possibilities in  all_combinations:
    temp_score_cap, temp_score_du, temp_score_fl, temp_score_te, temp_score_cal = 0, 0, 0, 0, 0
    for key in ingredients:
        temp_score_cap += ingredients[key].capacity*possibilities[key]
        temp_score_du += ingredients[key].durability*possibilities[key]
        temp_score_fl += ingredients[key].flavor*possibilities[key]
        temp_score_te += ingredients[key].texture*possibilities[key]
        temp_score_cal += ingredients[key].calories*possibilities[key]
    if temp_score_cap <= 0 or temp_score_du <= 0 or temp_score_fl <= 0 or temp_score_te <= 0:
        temp_score_cap = 0
        continue
    score.append(temp_score_cap*temp_score_du*temp_score_fl*temp_score_te)
    if temp_score_cal == 500:
        full_meal_cookies.append(temp_score_cap*temp_score_du*temp_score_fl*temp_score_te)


print(f"Points of the best scoring cookies: {max(score)}") #13.882.464
print(f"Points of the best scoring full meal cookies: {max(full_meal_cookies)}") #11.162.880 too low
