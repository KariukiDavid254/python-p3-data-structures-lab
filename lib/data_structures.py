spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    pass

def get_spiciest_foods(spicy_foods):
    pass

def print_spicy_foods(spicy_foods):
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    pass

def print_spiciest_foods(spicy_foods):
    pass

def get_average_heat_level(spicy_foods):
    pass

def create_spicy_food(spicy_foods, spicy_food):
    pass


def get_names(spicy_foods):
    names = []
    for food in spicy_foods:
        names.append(food["name"])
    return names

spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    }
]

food_names = get_names(spicy_foods)
print(food_names)



####SPICIEST FOOD
def get_spiciest_foods(spicy_foods):
    spiciest_foods = []
    for food in spicy_foods:
        if food["heat_level"] > 5:
            spiciest_foods.append(food)
    return spiciest_foods

spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    }
]

spiciest_foods = get_spiciest_foods(spicy_foods)
print(spiciest_foods)


####SPICY FOODS BY CUISINE
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None

spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    }
]

cuisine = "Thai"
spicy_food = get_spicy_food_by_cuisine(spicy_foods, cuisine)
if spicy_food:
    print(spicy_food)
else:
    print(f"No spicy food found for cuisine: {cuisine}")



####FOODS BY HEAT LEVEL
def average_heat_level(spicy_foods):
    total_heat_level = 0
    num_foods = len(spicy_foods)

    for food in spicy_foods:
        total_heat_level += food["heat_level"]

    if num_foods > 0:
        average = total_heat_level / num_foods
        return int(average)
    else:
        return 0

spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    }
]

avg_heat = average_heat_level(spicy_foods)
print(avg_heat)
