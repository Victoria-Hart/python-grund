# ==========================
# Variables in Python - Exercises
# ==========================

# 1. Simple variable
# Create a variable 'city' and assign it the name of your hometown. Print the value.
city = "Chicago"
print(city)

# 2. Naming rules
# The following variable names are invalid. Explain why and rewrite them so they work.
# 1variable = 100 variables must begin with a letter
var1 = 100

# my-variable = "hello" python has trouble reading -
my_variable = "hello"

# print = "hej" is a set command in python
salutation = "hej"



# 3. Case sensitivity
# What will be the output of the code below, and why?
# Age = 25
# age = 30
# print(Age) 25
# print(age) 30
# because python is case-sensitive


# 4. Dynamic typing
# Create a variable x and assign it an integer value.
# Then change x to a string value. Print both values.

x = 1
print(x)
x = "2"
print(x)

# 5. Multiple assignments
# Create three variables (a, b, c) in one line
# and assign them the values 10, 20, and "Thirty". Print them.

a = 10
b = 20
c = "Thirty"

print(a)
print(b)
print(c)

# 6. Type casting
# Create a variable num_str = "123".
# Convert it to int and float.
# Print both values and their types.

num_str = "123"
print(int(num_str))
print(float(num_str))

# 7. Object references
# Run the following code and explain the result.
# x = 5
# y = x
# x = 10
# print("x:", x)
# print("y:", y)

x = 5
y = x
x = 10
print("x:", x)
print("y:", y) 

# variable x was set and then y was set to variable x when it equals 5, then x is changed to 10 and y remains as 5 since no additional code was added to update its value


# 8. Swapping values
# Swap the values of two variables a and b without using a third variable.
a, b = 1, 2
a, b = b, a

# 9. String length
# Create a variable word with any word.
# Use len() to calculate the number of characters in the word and print the result.
word = "bananas" # 7
print(len(word))

# 10. Scope
# Study the code and explain why the output is what it is.
# x = "global"
#
# def my_func():
#     x = "local"
#     print("In function:", x)
#
# my_func()
# print("Outside function:", x)

x = "global"

def my_func():
     x = "local"
     print("In function:", x)

my_func()
print("Outside function:", x)
# x in my_func is a local variable and only exists inside that function while the first x variable is global and exists outside the function