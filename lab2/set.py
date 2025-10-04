# 1
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(f"Пересечение: {set1 & set2}")
print(f"Объединение: {set1 | set2}")

print('='*50)

# 2
text = input("Введите текст: ").split()
unique_words = set(text)
print(f"Уникальные слова: {unique_words}")

print('='*50)

# 3
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = set(list1) & set(list2)
print(f"Общие элементы: {common}")

print('='*50)

# 4
print(f"set1 подмножество set2: {set1.issubset(set2)}")

print('='*50)

# 5
num = int(input("Введите число для удаления меньше введенного числа: "))
my_set = {1, 5, 10, 15, 20}
my_set = {x for x in my_set if x >= num}
print(f"Множество после удаления: {my_set}")