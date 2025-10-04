import random

# 0
numbers = [random.randint(-59, 50) for _ in range(10)]
print(f"Случайный список: {numbers}")

print('='*50)

# 1
even_numbers = [x for x in numbers if x % 2 == 0]
print(f"Чётные элементы: {even_numbers}")

print('='*50)

# 2
print(f"Максимум: {max(numbers)}, Минимум: {min(numbers)}")

print('='*50)

# 3
user_list = []
for _ in range(5):
    user_list.append(int(input("Введите число: ")))
user_list.sort()
print(f"Отсортированный список: {user_list}")

print('='*50)

# 4
unique_list = []
for num in numbers:
    if num not in unique_list:
        unique_list.append(num)
print(f"Список без дубликатов: {unique_list}")

print('='*50)

# 5
if len(numbers) >= 2:
    numbers[0], numbers[-1] = numbers[-1], numbers[0]
print(f"После замены первого и последнего: {numbers}")