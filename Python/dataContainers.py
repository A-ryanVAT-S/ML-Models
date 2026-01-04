#Major data containers in Python are Lists, Tuples, Sets and Dictionaries.
#List uses [], Tuple uses (), Set uses {} and Dictionary uses {key:value} pairs.

###LISTS: A list is an ordered collection of items which is mutable (can be changed).
my_list = [1, 2, 3, "Hello", 4.5]  # Creating a list with mixed data types , we can do that
print(my_list)  # Output: [1, 2, 3, 'Hello', 4.5]

# Accessing elements in a list
first_element = my_list[0]  # 1
last_element = my_list[-1]  # 4.5
subset_list = my_list[1:4]  # [2, 3, 'Hello'] ([a:b] a=starting index, b=ending index-1)

#my_list. will show you all methods available for list.(count,extend,append,sort,remove etc)

# Modifying elements in a list
my_list[1] = 20  # Changing second element to 20
print(my_list)  # Output: [1, 20, 3, 'Hello', 4.5]

# Adding elements to a list
my_list.append("World")  # Adding an element at the end
print(my_list)  # Output: [1, 20, 3, 'Hello', 4.5, 'World']

# Removing elements from a list
my_list.remove(3)  # Removing element with value 3
print(my_list)  # Output: [1, 20, 'Hello', 4.5, 'World']


###TUPLES: A tuple is an ordered collection of items which is immutable (cannot be changed).
my_tuple = (1, 2, 3, "Hello", 4.5)  # Creating a tuple with mixed data types
print(my_tuple)  # Output: (1, 2, 3, 'Hello', 4.5)

# Accessing elements in a tuple
first_element = my_tuple[0]  # 1
last_element = my_tuple[-1]  # 4.5
subset_tuple = my_tuple[1:4]  # (2, 3, 'Hello')
my_tuple.__contains__(3)  # True , checks if element is present in tuple or not
length = len(my_tuple)  # 5 , returns length of tuple
#use dot (.) after tuple variable to see all methods available for tuple.There are so many methods.

# Tuples are immutable, so we cannot modify, add or remove elements.
# Trying to change an element will raise an error
# my_tuple[1] = 20  # This will raise a TypeError
# we can not add or remove elements from tuple as it is immutable.



###SETS: A set is an mutable unordered collection of unique items.(Unordered means it does not maintain the order of elements,Like first element, second element etc)

my_set = {1, 2, 3, "Hello", 4.5}  # Creating a set with mixed data types
print(my_set)  # Output: {1, 2, 3, 4.5, 'Hello'} (order may vary)

# Adding elements to a set
my_set.add("World")  # Adding an element
print(my_set)  # Output: {1, 2, 3, 4.5, 'Hello', 'World'}
#dot(.) after set variable will show you all methods available for set.(union,intersection,difference,remove,discard etc)

#set operations examples:
set_a=my_set.intersection({2,3,5})  # {2, 3} , returns common elements in both sets
set_b=my_set.union({5,6,7})  # {1, 2, 3, 4.5, 'Hello', 'World', 5, 6, 7} , returns all unique elements from both sets

#Set is unordered , so we cannot access elements using indexing like my_set[0] etc.
# set_a[2] # This will raise a TypeError



###DICTIONARIES: A dictionary is an unordered collection of key-value pairs. It is mutable.
my_dict = {"name": "Alice", "age": 25, "city": "New York"}  # Creating a dictionary
print(my_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}


# Accessing values in a dictionary
name = my_dict["name"]  # 'Alice'
age = my_dict.get("age")  # 25 , another way to access value
#dot(.) after dict variable will show you all methods available for dictionary.(keys,values,items,pop,update etc)

# Modifying values in a dictionary
my_dict["age"] = 26  # Changing age to 26
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York'}

# Adding key-value pairs to a dictionary
my_dict["country"] = "USA"  # Adding a new key-value pair
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'country': 'USA'}

# Removing key-value pairs from a dictionary
my_dict.pop("city")  # Removing the key 'city'
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'country': 'USA'}

# Dictionaries are unordered, so we cannot access items using indexing like my_dict[0] etc.
# my_dict[0]  # This will raise a TypeError

#Genral things:
# Use type() function to know the data type of any variable or data container.
# Use len() function to know the length of data containers like list, tuple, set, dictionary etc.
# we can nest data containers inside each other like list of tuples, dictionary of lists etc.
# we can use loops to iterate over data containers.
# Example: Iterating over a list
for item in my_list:
    print(item)

# Example: Iterating over a dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")

#These are the basic operations and methods for Lists, Tuples, Sets, and Dictionaries in Python.






