from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, fuel, condition):
        self.fuel = fuel
        self.condition = condition

    @property
    def is_working(self):
        return self.condition > 30

    @abstractmethod
    def __str__(self):
        pass

    def move(self, distance):
        if not self.is_working:
            print("Транспорт несправний. Рух неможливий.")
            return

        fuel_needed = distance

        if self.fuel < fuel_needed:
            print("Недостатньо пального.")
            return

        self.fuel -= fuel_needed
        self.condition -= distance * 0.5

        if self.condition < 0:
            self.condition = 0

        print(f"Транспорт проїхав {distance} км.")


class Car(Transport):
    def __init__(self, model):
        super().__init__(50, 100)
        self.model = model

    def __str__(self):
        return (f"Car: {self.model}, "
                f"fuel={self.fuel}, "
                f"condition={self.condition}")


class Truck(Transport):
    def __init__(self, name):
        super().__init__(120, 100)
        self.name = name

    def __str__(self):
        return (f"Truck: {self.name}, "
                f"fuel={self.fuel}, "
                f"condition={self.condition}")


class Motorcycle(Transport):
    def __init__(self, brand):
        super().__init__(20, 100)
        self.brand = brand

    def __str__(self):
        return (f"Motorcycle: {self.brand}, "
                f"fuel={self.fuel}, "
                f"condition={self.condition}")


class ServiceStation:
    def repair(self, transport_unit: Transport):
        transport_unit.condition += 25

        if transport_unit.condition > 100:
            transport_unit.condition = 100

        print("Транспорт відремонтовано.")



car = Car("BMW")
truck = Truck("Volvo")
motorcycle = Motorcycle("Honda")

print("Інформація про транспорт:")
print(car)
print(truck)
print(motorcycle)

print("\nПеревірка is_working:")
print(car.is_working)
print(truck.is_working)
print(motorcycle.is_working)

print("\n__dict__:")
print(car.__dict__)
print(truck.__dict__)
print(motorcycle.__dict__)

print("\nРух транспорту:")
car.move(20)
print(car)

truck.move(50)
print(truck)

motorcycle.move(10)
print(motorcycle)

print("\nВідсутність пального:")
motorcycle.move(50)

print("\nПоганий технічний стан:")
car.condition = 10
print(car.is_working)
car.move(5)

print("\nРемонт:")
service = ServiceStation()

service.repair(car)
print(car)

print("\nРемонт повністю зламаного транспорту:")
truck.condition = 0
print(truck)

service.repair(truck)
print(truck)

print("\nКілька ремонтів поспіль:")
service.repair(truck)
service.repair(truck)
service.repair(truck)
print(truck)