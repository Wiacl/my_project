import random
from collections import Counter

# 1
random_numbers = [random.randint(1, 50) for _ in range(20)]
unique_numbers = list(set(random_numbers))
print(f"Уникальные значения: {unique_numbers}")

print('='*50)

# 2
count_dict = {x: random_numbers.count(x) for x in set(random_numbers)}
print(f"Количество повторений: {count_dict}")

print('='*50)

# 3
words = ["apple", "cat", "elephant", "dog", "butterfly"]
long_words = {word for word in words if len(word) > 5}
print(f"Слова длиннее 5 символов: {long_words}")

print('='*50)

# 4
sentence = input("Введите предложение для подсчета вхождений: ").split()
word_count = {}
for word in sentence:
    word_count[word] = word_count.get(word, 0) + 1
print(f"Количество вхождений слов: {word_count}")

print('='*50)

# 5
numbers_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(numbers_with_duplicates))
print(f"Список без дубликатов: {unique_list}")

print('='*50)

# 6
products = {"хлеб": 50, "молоко": 120, "сыр": 300}
most_expensive = max(products, key=products.get)
print(f"Самый дорогой товар: {most_expensive}")

print('='*50)

# 7
names = ["Иван", "Мария", "Иван", "Петр", "Мария", "Мария"]
name_count = Counter(names)
most_common = name_count.most_common(1)[0]
print(f"Самое частое имя: {most_common[0]} (встречается {most_common[1]} раз)")

print('='*50)

# 8
text = input("Введите строку: ")
first_occurrence = {char: text.index(char) for char in text}
print(f"Первые вхождения символов: {first_occurrence}")