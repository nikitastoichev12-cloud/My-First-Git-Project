import requests

url = "https://script.google.com/macros/s/AKfycbzAYl-rgB5RAfwdDWetWeFPSbyHGBhomqSH25qQAE1AgxKsBVfZ_aCAyp8BLs1BkZ1c/exec"

response = requests.get(url)
data = response.json()

animals = data["animals"]

venomous_cost = 0
african_animals = 0

for animal in animals:

  
    if animal["is_venomous"].strip().lower() == "yes":
        venomous_cost += animal["care_cost"] * animal["count"]

    if animal["continent"].strip().lower() == "africa":
        african_animals += animal["count"]

print("Вартість догляду за отруйними тваринами:", venomous_cost)
print("Кількість африканських тварин:", african_animals)