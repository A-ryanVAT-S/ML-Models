#variable and data types in python

#python is a dynamically typed language, so you don't need to declare variable types explicitly.
#so you can directly assign values to variables.
a=10          #integer
b=3.14        #float
c="Hello"     #string
d=True        #boolean
e=None        #NoneType
print(type(a))  #output: <class 'int'>

#Rules for variable names:
#1. Variable names must start with a letter (a-z, A-Z) or an underscore (_).
#2. The rest of the variable name can contain letters, digits (0-9), or underscores.
#3. Variable names are case-sensitive (e.g., myVar and myvar are different variables).
#4. Variable names cannot be a reserved keyword in Python (e.g., if, else, while, for, etc.) or cannot contains spaces.

#Operators in Python

#Arithmetic Operators: +, -, *, /, %, ** (exponentiation), // (floor division)(it returns the largest integer less than or equal to the division result)
#Comparison Operators: ==, !=, >, <, >=, <=
#Logical Operators: and, or, not
#Assignment Operators: =, +=, -=, *=, /=, %=, **=, //=

#type conversion in python
x = 5          # integer
y = 2.5        # float
# Convert integer to float
x_float = float(x)
# Convert float to integer
y_int = int(y)
print(x_float)  # Output: 5.0
print(y_int)    # Output: 2
#similary str(int), bool(int), str(float), bool(float) etc can be used for type conversion.


#Input and Output in Python
#Input
name = input("Enter your name: ")  # takes input from user as string

#Output
print("Hello, " + name + "!")  # prints output to console
#formated output
age = 25
print("My name is {} and I am {} years old.".format(name, age))  # using format method so that we can insert variables in string
#another way of formated output (f-string)
print(f"My name is {name} and I am {age} years old.")  # using f-string for formatted output
# /n for new line , /t for tab space etc can be used in strings for formatting.


#Comments in Python
# This is a single-line comment
'''
This is a multi-line comment
which spans multiple lines.
You can use triple quotes for multi-line comments.
'''

#Indentation in Python
# Python uses indentation to define blocks of code. Indentation is typically 4 spaces.
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

#Incorrect indentation will raise an IndentationError also python dont uses braces to define code blocks like other languages.


#simple program in python
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(f"The sum of {a} and {b} is {a+b}")