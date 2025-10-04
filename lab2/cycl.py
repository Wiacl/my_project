# 1
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i * j}\t", end="")
    print()

print('='*50)

# 2
total = sum(range(1, 101, 2))
print(f"\nСумма нечётных чисел от 1 до 100: {total}")

print('='*50)

# 3
num = int(input("\nВведите число что бы посчитать его делители: "))
dividers = [i for i in range(1, num + 1) if num % i == 0]
print(f"Делители числа {num}: {dividers}")

print('='*50)

# 4
n = int(input("\nВведите число для факториала: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"Факториал {n} = {factorial}")

print('='*50)

# 5
n = int(input("\nВведите длину последовательности Фибоначчи: "))
fib = [0, 1]
for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])
print(f"Последовательность Фибоначчи: {fib[:n]}")