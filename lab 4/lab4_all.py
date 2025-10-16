print("1. Базовый класс: Создать класс Transport с атрибутами brand, speed, методом move() и __str__")
print("=" * 50)

class Transport:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    
    def move(self):
        print(f"Transport is moving at {self.speed} km/h")
    
    def __str__(self):
        return f"Transport: {self.brand}, Speed: {self.speed}"

print("2. Наследники: Создать классы Car и Bike")
print("=" * 50)

class Car(Transport):
    def __init__(self, brand, speed, seats):
        super().__init__(brand, speed)
        self.seats = seats
    
    def honk(self):
        print("Beep beep!")
    
    def move(self):
        print(f"Car {self.brand} is driving at {self.speed} km/h")
    
    def __str__(self):
        return f"Car: {self.brand}, Speed: {self.speed}, Seats: {self.seats}"
    
    def __len__(self):
        return self.seats
    
    def __eq__(self, other):
        if isinstance(other, Car):
            return self.speed == other.speed
        return False
    
    def __add__(self, other):
        if isinstance(other, Car):
            return self.speed + other.speed
        return NotImplemented

class Bike(Transport):
    def __init__(self, brand, speed, bike_type):
        super().__init__(brand, speed)
        self.type = bike_type
    
    def move(self):
        print(f"Bike {self.brand} is cycling at {self.speed} km/h")
    
    def __str__(self):
        return f"Bike: {self.brand}, Speed: {self.speed}, Type: {self.type}"

print("3. Магические методы: Добавить __len__, __eq__, __add__ в класс Car")
print("=" * 50)

print("4. Практика использования: Создание объектов и проверка методов")
print("=" * 50)

# 1. Создание объектов
transport1 = Transport("Generic", 60)
car1 = Car("Toyota", 120, 5)
car2 = Car("Honda", 100, 4)
bike1 = Bike("Giant", 25, "mountain")

# 2. Вывод объектов (работа __str__)
print("Объекты:")
print(transport1)
print(car1)
print(car2)
print(bike1)
print()

# 3. Проверка методов move() и honk()
print("Метод move():")
transport1.move()
car1.move()
bike1.move()
print()

print("Метод honk():")
car1.honk()
print()

# 4. Использование len(car)
print(f"Количество мест в car1: {len(car1)}")
print()

# 5. Сравнение двух машин
print(f"car1 == car2 (по скорости): {car1 == car2}")
print()

# 6. Сложение скоростей двух машин
print(f"Сумма скоростей car1 и car2: {car1 + car2}")
print()

# 7. Сложение машины и велосипеда
print("Попытка сложить машину и велосипед:")
try:
    result = car1 + bike1
    print(f"Результат: {result}")
except TypeError as e:
    print(f"Ошибка: {e}")
print("Объяснение: Метод __add__ в классе Car проверяет, является ли второй объект экземпляром Car.")
print("Если нет - возвращает NotImplemented, что вызывает TypeError")

print("=" * 50)
print("5. Дополнительное задание: Список объектов и вызов метода move()")
print("=" * 50)

# Создание списка объектов
transports = [
    Transport("Generic", 50),
    Car("BMW", 150, 4),
    Car("Ford", 110, 5),
    Bike("Trek", 30, "road"),
    Bike("Specialized", 20, "mountain")
]

# Вызов метода move() для каждого объекта
print("Вызов метода move() для всех объектов в списке:")
for transport in transports:
    transport.move()

