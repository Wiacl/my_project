squares = [x**2 for x in range(1, 11)]
print(squares)
print('='*50)

even_numbers = [x for x in range(1, 20) if x % 2 == 0]
print(even_numbers)
print('='*50)

words = ["python", "Java", "c++", "Rust", "go"]
result = [word.upper() for word in words if len(word) > 3]
print(result)
print('='*50)

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

print('='*50)
    

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(5):
    print(num)

print('='*50)
    
    
from decimal import Decimal, getcontext

getcontext().prec = 10

P = Decimal(input("Начальная сумма вклада: "))
r = Decimal(input("Процентная ставка годовых: "))
t = Decimal(input("Срок вклада (в годах): "))

S = P * (1 + r / (12 * 100)) ** (12 * t)
profit = S - P

print(f"Итоговая сумма: {S:.2f} руб.")
print(f"Общая прибыль: {profit:.2f} руб.")
print('='*50)


from fractions import Fraction

f1 = Fraction(3, 4)
f2 = Fraction(5, 6)

print('='*50)
print(f"Сложение: {f1 + f2}")
print(f"Вычитание: {f1 - f2}")
print(f"Умножение: {f1 * f2}")
print(f"Деление: {f1 / f2}")
print('='*50)

from datetime import datetime

now = datetime.now()
print('='*50)
print(f"Текущая дата и время: {now}")
print(f"Текущая дата: {now.date()}")
print(f"Текущее время: {now.time()}")
print('='*50)

from datetime import datetime, date

birthday = date(1990, 5, 15)  # замените на свою дату рождения
today = date.today()

days_passed = (today - birthday).days
next_birthday = date(today.year, birthday.month, birthday.day)

if next_birthday < today:
    next_birthday = date(today.year + 1, birthday.month, birthday.day)

days_to_birthday = (next_birthday - today).days

print('='*50)
print(f"Дней прошло с рождения: {days_passed}")
print(f"Дней до следующего дня рождения: {days_to_birthday}")
print('='*50)

from datetime import datetime

def format_date(dt):
    months = {
        1: "января", 2: "февраля", 3: "марта", 4: "апреля",
        5: "мая", 6: "июня", 7: "июля", 8: "августа",
        9: "сентября", 10: "октября", 11: "ноября", 12: "декабря"
    }
    return f"Сегодня {dt.day} {months[dt.month]} {dt.year} года, время: {dt.strftime('%H:%M')}"

print('='*50)
print(format_date(datetime.now()))
