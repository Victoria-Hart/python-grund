# ==========================
# Python Operators - Exercises
# ==========================

# 1. Arithmetic Operators
# Create two variables a = 8, b = 3
# Perform and print the result of:
# addition, subtraction, multiplication, division,
# floor division, modulus, exponentiation

a = 8
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

# 2. Comparison Operators
# Create two variables a = 7, b = 10
# Print the result of:
# a > b
# a < b
# a == b
# a != b
# a >= b
# a <= b

a = 7
b = 10
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

# 3. Logical Operators
# Create two boolean variables a = True, b = False
# Print the result of:
# a and b
# a or b
# not a

a = True
b = False
print(a and b)
print(a or b)
print(not a)


# 4. Assignment Operators
# Create a variable a = 5
# Use assignment operators to perform:
# - b = a
# - b += a
# - b -= a
# - b *= a
# Print the value of b after each operation

a = 5
b = a
print(b)
b += a
print(b)
b -= a
print(b)
b *= a
print(b)

# 5. Identity Operators
# Create variables a = 10, b = 20, c = a
# Print the result of:
# a is b
# a is not b
# a is c
# a is not c

a = 10
b = 20
c = a
print(a is b)
print(a is not b)
print(a is c)
print(a is not c)


# 6. Membership Operators
# Create a list: my_list = [5, 10, 15, 20]
# Create two variables x = 25, y = 10
# Check and print whether x is in my_list
# Check and print whether y is in my_list

my_list = [5, 10, 15, 20]

x = 25
y = 10

if x in my_list:
    print("x is in my_list") #False
else:
    print("x is NOT in my list") #True

if y in my_list:
    print("y is in my list") #True
else:
    print("y is NOT in my list") #False