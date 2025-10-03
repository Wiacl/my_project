squares = [x**2 for x in range(1, 11)]
print(squares)

even_numbers = [x for x in range(1, 20) if x % 2 == 0]
print(even_numbers)

words = ["python", "Java", "c++", "Rust", "go"]
result = [word.upper() for word in words if len(word) > 3]
print(result)

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