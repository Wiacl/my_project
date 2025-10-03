squares = [x**2 for x in range(1, 11)]
print(squares)

even_numbers = [x for x in range(1, 20) if x % 2 == 0]
print(even_numbers)

words = ["python", "Java", "c++", "Rust", "go"]
result = [word.upper() for word in words if len(word) > 3]
print(result)

class Countdown:
    def __init__(self, n):
        self.n = n
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n == 0:
            raise StopIteration
        current = self.n
        self.n -= 1
        return current

for x in Countdown(5):
    print(x)
    

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(5):
    print(num)
    
    
from decimal import Decimal, getcontext

getcontext().prec = 10

P = Decimal(input("Начальная сумма вклада: "))
r = Decimal(input("Процентная ставка годовых: "))
t = Decimal(input("Срок вклада (в годах): "))

S = P * (1 + r / (12 * 100)) ** (12 * t)
profit = S - P

print(f"Итоговая сумма: {S:.2f} руб.")
print(f"Общая прибыль: {profit:.2f} руб.")


from fractions import Fraction

f1 = Fraction(3, 4)
f2 = Fraction(5, 6)

print(f"Сложение: {f1 + f2}")
print(f"Вычитание: {f1 - f2}")
print(f"Умножение: {f1 * f2}")
print(f"Деление: {f1 / f2}")

from datetime import datetime

now = datetime.now()
print(f"Текущая дата и время: {now}")
print(f"Текущая дата: {now.date()}")
print(f"Текущее время: {now.time()}")

from datetime import datetime, date

birthday = date(1990, 5, 15)  # замените на свою дату рождения
today = date.today()

days_passed = (today - birthday).days
next_birthday = date(today.year, birthday.month, birthday.day)

if next_birthday < today:
    next_birthday = date(today.year + 1, birthday.month, birthday.day)

days_to_birthday = (next_birthday - today).days

print(f"Дней прошло с рождения: {days_passed}")
print(f"Дней до следующего дня рождения: {days_to_birthday}")