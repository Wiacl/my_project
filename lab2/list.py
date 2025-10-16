import random

# 0
numbers = [random.randint(-59, 50) for _ in range(10)]
print(f"Случайный список: {numbers}", "\n")

print('='*50)

# 1
print("Создать список из 10 чисел и вывести только чётные элементы.", "\n")
even_numbers = [x for x in numbers if x % 2 == 0]
print(f"Чётные элементы: {even_numbers}", "\n")

print('='*50)

# 2
print("Найти максимальное и минимальное число в списке.", "\n")

print(f"Максимум: {max(numbers)}, Минимум: {min(numbers)}", "\n")

print('='*50)

# 3
print("Запросить у пользователя 5 чисел, сохранить в список (используйте .append()), отсортировать его и вывести.", "\n")

user_list = []
for _ in range(5):
    user_list.append(int(input("Введите число(всего 5): ")))
user_list.sort()
print(f"Отсортированный список: {user_list}", "\n")

print('='*50)

# 4
print("Удалить из списка все дубликаты", "\n")

print(f"Исходный список: {numbers}", "\n")

unique_list = []
for num in numbers:
    if num not in unique_list:
        unique_list.append(num)
print(f"Список без дубликатов: {unique_list}", "\n")

print('='*50)

# 5
print("Поменять местами первый и последний элемент списка.", "\n")

if len(numbers) >= 2:
    numbers[0], numbers[-1] = numbers[-1], numbers[0]
print(f"После замены первого и последнего: {numbers}", "\n")