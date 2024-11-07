# Define a generator function that generates Fibonacci numbers indefinitely
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Create a Fibonacci sequence generator
fib_gen = fibonacci_generator()

# Generate and print the first 10 Fibonacci numbers
for _ in range(10):
    print(next(fib_gen))

# Define a generator expression to generate squares of numbers within a range
squares_gen = (x ** 2 for x in range(1, 6))

# Iterate and print the squares
for square in squares_gen:
    print(square)
