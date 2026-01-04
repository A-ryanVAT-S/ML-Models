#STRINGS BASICS

# Creating strings
my_string = "Hello, World!" # we can use '', " ", or """  """ all valid

# Accessing characters in a string
first_char = my_string[0]  # H
last_char = my_string[-1]  # !

# Slicing strings
first_5 = my_string[0:5]  # Hello   ([a:b] a=starting index, b=ending index-1)
full_string = my_string[:]  # Hello, World!
last_6 = my_string[-6:]  # World!  # if we do [:a] it means from starting to a-1 index,[a:] means from a to end of string

# String methods
upper_string = my_string.upper()  # "HELLO, WORLD!"
lower_string = my_string.lower()  # "hello, world!"
replace_string = my_string.replace("World", "Python")  # "Hello, Python!"
split_string = my_string.split(", ")  # ['Hello', 'World!'] # splits string into list based on delimiter i.e space , comma. 
#If there would be comma only without space it would have been ['Hello', 'World!']

start_index = my_string.find("World")  # 7  # returns starting index of substring, if not found returns -1
length = len(my_string)  # 13  # returns length of string
starts_with_hello = my_string.startswith("Hello")  # True  # checks if string starts with given substring
ends_with_exclamation = my_string.endswith("!")  # True  # checks if string ends with given substring
#so many methods are there just str. and then dot(.) will show you all methods available for string.



# String concatenation
greeting = "Hello"
name = "Alice"
full_greeting = greeting + ", " + name + "!"  # "Hello, Alice!" , simple concatenation using +

# String are immutable
# Trying to change a character in the string will raise an error
# my_string[0] = "h"  # This will raise a TypeError



