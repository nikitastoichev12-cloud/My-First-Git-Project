import requests

url = "http://127.0.0.1:8000/animals"

response = requests.get(url)
animals = response.json()

venomous_cost = 0
african_animals = 0

for animal in animals:

    if animal["is_venomous"] == "Yes":
        venomous_cost += animal["care_cost"] * animal["count"]

    if animal["continent"] == "Africa":
        african_animals += animal["count"]

print("Cost of caring for venomous animals:", venomous_cost)
print("Number of African animals:", african_animals)