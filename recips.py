import requests

url = "https://dummyjson.com/recipes"
data = requests.get(url).json()["recipes"]

# 1. пицца
pizza_recipes = []
for r in data:
    if "pizza" in r["name"].lower():
        pizza_recipes.append(r["name"])

print("Піцци:", pizza_recipes)

# 2. итальянская кухня
italian_count = 0
for r in data:
    if r.get("cuisine") == "Italian":
        italian_count += 1

print("Італійська кухня:", italian_count)

# 3. самая коларийная еда
max_cal = 0
max_dish = ""

for r in data:
    if r.get("caloriesPerServing", 0) > max_cal:
        max_cal = r["caloriesPerServing"]
        max_dish = r["name"]

print("Найкалорійніша:", max_dish, max_cal)

# 4 190 град
temp_dishes = []
for r in data:
    instructions = r.get("instructions", [])
    if instructions and "190" in instructions[0]:
        temp_dishes.append(r["name"])

print("При 190°C:", temp_dishes)

# 5 отзывы
total_reviews = 0
for r in data:
    total_reviews += r.get("reviewCount", 0)

print("Всього відгуків:", total_reviews)