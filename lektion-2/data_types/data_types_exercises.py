# ==========================
# Python Data Types - Exercises
# ==========================

# 1. Numeric Datatypes
# Create three variables:
# 1. int_var = 10
# 2. float_var = 10.5
# 3. complex_var = 3 + 4j
# Print each variable and its type.

int_var = 10
float_var = 10.5
complex_var = 3 + 4j

print(type(int_var))
print(type(float_var))
print(type(complex_var))

# 2. Strings
# Create a string variable my_string = "Python is fun"
# Print the first, second, and last character using indexing.

my_string = "Python is fun"
print(my_string[0])
print(my_string[1])
print(my_string[-1])

# 3. Lists
# Create a list my_list = [1, 2, 3, 'Python', 'AI']
# Print:
# - first element
# - last element using negative indexing
# - second-to-last element using negative indexing

my_list = [1, 2, 3, 'Python', 'AI']
print(my_list[0])
print(my_list[-1])
print(my_list[-2])

# 4. Tuples
# Create a tuple my_tuple = ("apple", "banana", "cherry")
# Print:
# - first element
# - last element
# Try to change the first element (observe what happens)

my_tuple = ("apple", "banana", "cherry")
print(my_tuple[0])
print(my_tuple[-1])

# 5. Booleans
# Create two variables: is_true = True, is_false = False
# Print the type of both variables

is_true = True
is_false = False

print(type(is_true))
print(type(is_false))

# 6. Sets
# Create a set my_set = {"apple", "banana", "cherry", "apple"}
# Print the set
# Add "orange" to the set and print it again

my_set = {"apple", "banana", "cherry", "apple"}
print(my_set)
my_set = my_set.add("orange")
print(my_set)

# 7. Dictionaries
# Create a dictionary my_dict with keys and values:
# 1: "One", 2: "Two", 3: "Three"
# Print:
# - the value of key 2
# - use the get() method to get value of key 3

my_dict = {1: "One", 2: "Two", 3: "Three"}
print(my_dict[2])
print(my_dict.get(3))

