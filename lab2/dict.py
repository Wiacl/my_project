# 1
students = {"Иван": 4, "Мария": 5, "Петр": 3}
average = sum(students.values()) / len(students)
print(f"Средний балл: {average:.2f}")

print('='*50)

# 2
text = input("Введите строку для подсчета букв: ")
char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1
print(f"Количество букв: {char_count}")

print('='*50)

# 3
squares = {x: x**2 for x in range(1, 11)}
print(f"Квадраты чисел: {squares}")

print('='*50)

# 4
keys = ['a', 'b', 'c']
values = [1, 2, 3]
combined_dict = dict(zip(keys, values))
print(f"Объединённый словарь: {combined_dict}")