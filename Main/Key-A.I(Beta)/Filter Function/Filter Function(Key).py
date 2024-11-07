# Create a list of squares for even numbers in the range 1 to 10
even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(even_squares)

# Create a list of tuples containing prime numbers and their squares in the range 1 to 20
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_squares = [(x, x ** 2) for x in range(1, 21) if is_prime(x)]
print(prime_squares)

# Flatten a list of lists using nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [element for row in matrix for element in row]
print(flattened)

# Create a dictionary using a dictionary comprehension
words = ["apple", "banana", "cherry"]
word_lengths = {word: len(word) for word in words}
print(word_lengths)
