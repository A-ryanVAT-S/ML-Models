# CONDITIONS, LOOPS, AND FUNCTIONS - Basic Python Revision
"""THIS IS A DOC STRING EXPLAINING THE PURPOSE OF THE FILE and in functions we use doc strings to show what the function does."""

### CONDITIONS
def check_number(num):
    """if-elif-else example"""
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

def is_teenager(age):
    """Logical operators: and, or, not"""
    return age >= 13 and age <= 19

def nested_conditions(score):
    """Nested if statements"""
    if score >= 0:
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"
    else:
        return "Invalid score"


### LOOPS
def print_range(n):
    """For loop with range"""
    for i in range(n):
        print(i, end=" ")
    print()

def countdown(n):
    """While loop"""
    while n > 0:
        print(n, end=" ")
        n -= 1
    print("Done!")

def find_first_even(numbers):
    """break and continue"""
    for num in numbers:
        if num % 2 != 0:
            continue  # Skip odd numbers
        return num  # Return first even
    return None


### BASIC FUNCTIONS
def greet(name):
    """Simple function"""
    return f"Hello, {name}!"

def power(base, exponent=2):
    """Default parameter"""
    return base ** exponent

def sum_all(*args):
    """*args: variable positional arguments (tuple)"""
    return sum(args)

def build_profile(name, age, **kwargs):
    """**kwargs: variable keyword arguments (dict)"""
    profile = {"name": name, "age": age}
    profile.update(kwargs)
    return profile


### IMPORTANT FUNCTION CONCEPTS
# Lambda functions
square = lambda x: x * x
add = lambda a, b: a + b

# map, filter and reduce
from functools import reduce
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
reduced= reduce(lambda x, y: x + y, numbers) # Sum of all numbers

# Recursion
def factorial(n):
    """Recursive function"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Generator (yield)
def fibonacci(n):
    """Generator function - yields values one by one"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Closure
def make_multiplier(factor):
    """Closure - inner function remembers outer variable"""
    def multiplier(x):
        return x * factor
    return multiplier

# Decorator
def uppercase(func):
    """Decorator - wraps function to modify behavior"""
    def wrapper(name):
        return func(name).upper()
    return wrapper

@uppercase
def say_hi(name):
    return f"hi {name}"


### ADVANCED CONCEPTS (Good to Know)
# Type hints
def typed_divide(a: float, b: float) -> float:
    return a / b

# Exception handling
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

# global and nonlocal
counter = 0
def increment_counter():
    global counter
    counter += 1

def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment



