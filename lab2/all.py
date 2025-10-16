import random
from collections import Counter

# 1
print("Сгенерировать список из 20 случайных чисел и вывести только уникальные значения.", "\n")
random_numbers = [random.randint(1, 50) for _ in range(20)]
unique_numbers = list(set(random_numbers))
print(f"Исходный список: {random_numbers}\n")
print(f"Уникальные значения: {unique_numbers}", "\n")

print('='*50)

# 2
print("Создать словарь, где ключи – это элементы списка, а значения – количество их повторений.", "\n")
count_dict = {x: random_numbers.count(x) for x in set(random_numbers)}
print(f"Количество повторений: {count_dict}", "\n")

print('='*50)

# 3
print("Дан список слов. Создать множество из слов, длина которых больше 5 символов.", "\n")

words = ["apple", "cat", "elephant", "dog", "butterfly"]
long_words = {word for word in words if len(word) > 5}
print(f"Слова длиннее 5 символов: {long_words}", "\n")

print('='*50)

# 4
print("Ввести предложение. Сохранить в словарь количество вхождений каждого слова.", "\n")
sentence = input("Введите предложение для подсчета вхождений: ").split()
word_count = {}
for word in sentence:
    word_count[word] = word_count.get(word, 0) + 1
print(f"Количество вхождений слов: {word_count}", "\n")

print('='*50)

# 5
print("Создать список чисел, преобразовать его в множество и обратно в список (убрав дубликаты).", "\n")

numbers_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(numbers_with_duplicates))
print(f"Список без дубликатов: {unique_list}", "\n")

print('='*50)

# 6
print("Дан словарь товар – цена. Найти самый дорогой товар.", "\n")

products = {"хлеб": 50, "молоко": 120, "сыр": 300}
most_expensive = max(products, key=products.get)
print(f"Самый дорогой товар: {most_expensive}", "\n")

print('='*50)

# 7
print("Дан список имён. Определить, какие из имён встречаются более одного раза. Какое имя встречается чаще всего.", "\n")
names = ["Иван", "Мария", "Иван", "Петр", "Мария", "Мария"]
name_count = Counter(names)
most_common = name_count.most_common(1)[0]
print(f"Самое частое имя: {most_common[0]} (встречается {most_common[1]} раз)", "\n")

print('='*50)

# 8
print("Запросить у пользователя строку и составить словарь: символ → индекс его первого вхождения.", "\n")

text = input("Введите строку: ")
first_occurrence = {char: text.index(char) for char in text}
print(f"Первые вхождения символов: {first_occurrence}", "\n")