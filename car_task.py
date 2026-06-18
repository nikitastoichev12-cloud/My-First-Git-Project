car = {
    "model": "BMW M5 Competition",
    "price": 3900000,
    "engine_volume": 4.4,
    "full_weight": 2300,
    "max_speed": 305,
    "fuel_consumption": 11.5,

    "interior_features": [
        "Спортивні сидіння M",
        "Карбонові вставки",
        "Цифрова панель приладів",
        "Клімат-контроль 4-зонний",
        "Преміальна аудіосистема"
    ],

    "trunk": {
        "volume": 530,
        "volume_seats_folded": 1530
    }
}

# добавляем инфомацию

car["trailer_max_weight"] = 2000

# вывод данных

print("Модель авто:", car.get("model"))
print("Ціна:", f"{car.get('price'):,} грн")
print("Перша опція інтер'єру:", car.get("interior_features")[0])
print("Багажник зі складеними сидіннями:", car["trunk"]["volume_seats_folded"])

# страховка 0,5 проц

insurance = car["price"] * 0.005
car["insurance"] = insurance

print("Страховка:", f"{insurance:,.0f} грн")

# поездка 200 километров


distance = 200
fuel_price = 93

fuel_used = (car["fuel_consumption"] * distance) / 100
trip_cost = fuel_used * fuel_price

print("Вартість поїздки на 200 км:", f"{trip_cost:.2f} грн")