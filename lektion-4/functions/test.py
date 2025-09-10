x = 123

def display():
    x = 42
    print(x)
    print(globals()['x'])

print(x) # global variable 123
display() # print local variable 42, then global variable 123