# Day 2 - Python Functions

# Function to add two numbers
def add(a, b):
    return a + b

# Function to find square of a number
def square(n):
    return n * n

# Function to check even or odd
def even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Function to find factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# Function to find the largest of two numbers
def largest(a, b):
    if a > b:
        return a
    else:
        return b


# Main Program
print("Addition:", add(10, 20))
print("Square:", square(5))
print("Even/Odd:", even_or_odd(7))
print("Factorial:", factorial(5))
print("Largest:", largest(15, 20))