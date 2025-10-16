# 1
print("Создать словарь с именами студентов и их оценками, вывести средний балл.", "\n")

students = {"Иван": 4, "Мария": 5, "Петр": 3}
average = sum(students.values()) / len(students)
print(f"Средний балл: {average:.2f}", "\n")

print('='*50)

# 2
print("""Подсчитать количество каждой буквы в строке (словарь: буква → количество). 
Пользователь сначала с помощью input() вводит строку, затем вы создаете необходимый словарь.""", "\n")

text = input("Введите строку для подсчета букв: ")
char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1
print(f"Количество букв: {char_count}", "\n")

print('='*50)

# 3
print("Создать словарь, где ключи – это числа от 1 до 10, а значения – их квадраты.", "\n")

squares = {x: x**2 for x in range(1, 11)}
print(f"Квадраты чисел: {squares}", "\n")

print('='*50)

# 4
print("Составить словарь из двух списков: список ключей и список значений.", "\n")

keys = ['a', 'b', 'c']
values = [1, 2, 3]
combined_dict = dict(zip(keys, values))
print(f"Объединённый словарь: {combined_dict}", "\n")