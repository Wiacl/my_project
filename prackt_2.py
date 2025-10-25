print(f"1. Декоратор логирования: Создать декоратор logger(func)\n")


def logger(func):
    def wrapper(*args, **kwargs):                   #позиционные, именнованные
        # Перед вызовом функции
        print(f"Вызов функции {func.__name__} с аргументами {args} и {kwargs}")
        
        # Выполнение функции
        result = func(*args, **kwargs)
        
        # После выполнения функции
        print(f"Функция {func.__name__} вернула {result}")
        return result
    return wrapper

print("Применение декоратора к функциям:")

@logger
def add(a, b):
    return a + b

@logger
def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b

@logger
def greet(name):
    return f"Привет, {name}!"

# Тестирование функций с декоратором
print("Тестирование функции add:")
result1 = add(5, 3)
print()

print("Тестирование функции divide:")
result2 = divide(10, 2)
print()

print("Тестирование функции divide с делением на ноль:")
result3 = divide(10, 0)
print()

print("Тестирование функции greet:")
result4 = greet("Анна")
print()

print("=" * 50)

print(f"2. Декоратор доступа: Создать декоратор require_role(allowed_roles)\n")


def require_role(allowed_roles):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if user.get('role') in allowed_roles:
                return func(user, *args, **kwargs)
            else:
                print(f"Доступ запрещён пользователю {user['name']}")
                return None
        return wrapper
    return decorator

print(f"Пример использования декоратора require_role:\n")

 
@require_role(['admin'])
@logger
def delete_database(user):
    print(f"База данных удалена пользователем {user['name']}")
    return "Операция выполнена успешно"

@require_role(['admin', 'manager'])
def edit_settings(user):
    print(f"Настройки изменены пользователем {user['name']}")
    return "Настройки обновлены"

@require_role(['admin', 'manager'])
def edit_database(user):
    print(f"База данных изменена пользователем {user['name']}")
    return "Операция выполнена успешно"

@require_role(['user', 'admin', 'manager'])
def view_data(user):
    print(f"Данные просмотрены пользователем {user['name']}")
    return "Данные загружены"

print(f"Создание пользователей с разными ролями:\n")


# Создание пользователей
users = [
    {'name': 'Виталий', 'role': 'admin'},
    {'name': 'Елена', 'role': 'manager'},
    {'name': 'Антон', 'role': 'user'},
    {'name': 'Ольга', 'role': 'guest'}
]

print("=" * 50)
print(f"Тестирование доступа для разных пользователей:\n")


# Тестирование функции delete_database для разных пользователей
print(f"Функция delete_database (требует роль 'admin'):\n")

for user in users:
    print(f"Пользователь: {user['name']}, роль: {user['role']}")
    result = delete_database(user)
    if result:
        print(f"Результат: {result}")
    print("-" * 30)

print(f"Функция edit_database (требует роль 'admin/manager'):\n")

for user in users:
    print(f"Пользователь: {user['name']}, роль: {user['role']}")
    result = edit_database(user)
    if result:
        print(f"Результат: {result}")
    print("-" * 30)
    
print()

print(f"Функция edit_settings (требует роли 'admin' или 'manager'):\n")

for user in users:
    print(f"Пользователь: {user['name']}, роль: {user['role']}")
    result = edit_settings(user)
    if result:
        print(f"Результат: {result}")
    print("-" * 30)


print()

print(f"Функция view_data (требует роли 'user', 'admin' или 'manager'):\n")

for user in users:
    print(f"Пользователь: {user['name']}, роль: {user['role']}")
    result = view_data(user)
    if result:
        print(f"Результат: {result}")
    print("-" * 30)

print("=" * 50)

print(f"Тестирование функций с дополнительными аргументами:\n")

@require_role(['admin'])
def create_user(admin_user, username, email):
    print(f"Пользователь {username} создан администратором {admin_user['name']}")
    return f"Создан пользователь: {username} ({email})"

admin_user = {'name': 'Сергей', 'role': 'admin'}
regular_user = {'name': 'Дмитрий', 'role': 'user'}

print("Создание пользователя администратором:")
result = create_user(admin_user, "new_user", "new@example.com")
print(f"Результат: {result}")
print()

print("Попытка создания пользователя обычным пользователем:")
result = create_user(regular_user, "another_user", "another@example.com")
print(f"Результат: {result}")