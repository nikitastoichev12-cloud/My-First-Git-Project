class Car:
    def __init__(self, model, age, owner=None, fuel=0):
        self.model = model
        self.age = age
        self.owner = owner
        self.fuel = fuel
        self.car_id = id(self)

    def __str__(self):
        return (f"Авто: {self.model}, "
                f"Вік: {self.age} років, "
                f"Власник: {self.owner}, "
                f"Бензин: {self.fuel} л, "
                f"ID: {self.car_id}")

    def refuel(self, amount):
        """Заправка авто"""
        self.fuel += amount

    @property
    def condition(self):
        """Характеристика авто за віком"""
        if self.age <= 3:
            return "Нове авто"
        elif self.age <= 10:
            return "Середній стан"
        else:
            return "Старе авто"

    @property
    def fuel_status(self):
        """Стан пального"""
        if self.fuel < 10:
            return "Потрібно заправитись"
        elif self.fuel < 30:
            return "Достатньо бензину"
        else:
            return "Можна їхати далеко"



car1 = Car("BMW X5", 2, "Іван", 15)
car2 = Car("Audi A6", 12, "Петро", 5)


print("ID car1:", id(car1))
print("ID car2:", id(car2))


print("\nСловник car1:")
print(car1.__dict__)

print("\nСловник car2:")
print(car2.__dict__)


print("\nІнформація про авто:")
print(car1)
print(car2)


car1.fuel = 20
print("\nПісля зміни пального car1:")
print(car1)


car2.refuel(25)
print("\nПісля заправки car2:")
print(car2)


print("\nСтан автомобілів:")
print(f"{car1.model}: {car1.condition}")
print(f"{car2.model}: {car2.condition}")


print("\nСтатус пального:")
print(f"{car1.model}: {car1.fuel_status}")
print(f"{car2.model}: {car2.fuel_status}")


print("\nПорівняння пального:")
if car1.fuel > car2.fuel:
    print(f"У {car1.model} більше бензину.")
elif car2.fuel > car1.fuel:
    print(f"У {car2.model} більше бензину.")
else:
    print("Кількість бензину однакова.")