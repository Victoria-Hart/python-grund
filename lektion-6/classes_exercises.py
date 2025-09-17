"""
Lab 6 - Classes Practice
"""

# ----------------------
# Section 1 . Classes
# ----------------------

# ----------------------
# Exercises
# ----------------------

def ex_1_1():
    """
    Create a class `Car` with a property `make` set to "Toyota".
    Add a method `get_make()` that returns the make of the car.
    Return the result of calling `get_make()` on an instance.
    """
    # TODO: Write your code here
    class Car:
        def __init__(self):
            self.make = "Toyota"

        def get_make(self):
            return self.make


def ex_1_2():
    """
    Add properties `model` and `year` to the Car class with values "Corolla" and 2020.
    Add a method `get_info()` that returns "Toyota Corolla, 2020".
    Return the result of calling `get_info()` on an instance.
    """
    # TODO: Write your code here
    class Car:
        def __init__(self):
            self.make = "Toyota"
            self.model = "Corolla"
            self.year = 2020

        def get_make(self):
            return self.make

        def get_info(self):
            return f"{self.make} {self.model}, {self.year}"

    car1 = Car()
    return car1.get_info()

def ex_1_3():
    """
    Create a class `Rectangle` with properties `width` and `height`.
    Add a method `area()` that returns the area of the rectangle.
    Return the area of a rectangle with width=5 and height=10.
    """
    # TODO: Write your code here
    class Rectangle():
        def __init__(self):
            self.width = 5
            self.height = 10

        def area(self):
            return self.width * self.height
    
    rectangle1 = Rectangle()
    return rectangle1.area()


def ex_1_4():
    """
    Add a method `perimeter()` to Rectangle that returns the perimeter.
    Return the perimeter of a rectangle with width=5 and height=10.
    """
    # TODO: Write your code here
    class Rectangle():
        def __init__(self):
            self.width = 5
            self.height = 10

        def area(self):
            return self.width * self.height

        def perimeter(self):
            return (self.width*2) + (self.height*2)
    
    rectangle1 = Rectangle()
    return rectangle1.perimeter()

def ex_1_5():
    """
    Create a class `BankAccount` with properties `owner` and `balance` (default 0).
    Add a method `deposit(amount)` that adds to balance.
    Return the balance after depositing 100.
    """
    # TODO: Write your code here
    class BankAccount():
        def __init__(self):
            self.owner = "owner"
            self.balance = 0

        def deposit(self, amount):
            self.balance += amount
            return self.balance

    my_account = BankAccount()
    return my_account.deposit(100)


def ex_1_6():
    """
    Add a method `withdraw(amount)` to BankAccount.
    It should subtract from balance if sufficient funds, otherwise do nothing.
    Return the balance after withdrawing 50 from an account with 100 balance.
    """
    # TODO: Write your code here
    class BankAccount():
        def __init__(self):
            self.owner = "owner"
            self.balance = 100

        def deposit(self, amount):
            self.balance += amount
            return self.balance

        def withdraw(self, amount):
            if self.balance >= amount:
                self.balance -= amount
            else:
                pass
            return self.balance

    my_account = BankAccount()
    return my_account.withdraw(50)

def ex_1_7():
    """
    Create a class `Student` with properties `name` and `grades` (a list).
    Add a method `average()` that returns the average grade.
    Return the average for a student with grades [80, 90, 100].
    """
    # TODO: Write your code here
    class Student():
        def __init__(self):
            self.name = "Student"
            self.grades = [80, 90, 100]

        def average(self):
            return sum(self.grades) / len(self.grades)

    student1 = Student()
    return student1.average()

def ex_1_8():
    """
    Add a method `add_grade(grade)` to Student that appends to the grades list.
    Add grade 95 to the previous student and return the new average.
    """
    # TODO: Write your code here
    class Student():
        def __init__(self):
            self.name = "Student"
            self.grades = [80, 90, 100]

        def average(self):
            return sum(self.grades) / len(self.grades)

        def add_grade(self, grade):
            return self.grades.append(grade)

    student1 = Student()
    student1.add_grade(95)
    return student1.average()

def ex_1_9():
    """
    Create a class `Dog` with properties `name` and `age`.
    Add a method `bark(times)` that returns "Woof!" repeated `times` times,
    separated by spaces, followed by the dog's name in parentheses, e.g.
    "Woof! Woof! (Bob)" if times=2.
    
    Return the result of calling `bark(3)` for a dog named "Bob".
    """
    # TODO: Write your code here
    class Dog():
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def bark(self, times):
            return ("Woof! " * times).strip() + f" ({self.name})"

    dog1 = Dog("Bob", 4)
    return dog1.bark(3)

def ex_1_10():
    """
    Add a method `birthday()` to Dog that:
    - increases the age by 1
    - returns a string: "Happy birthday {name}! You are now {age} years old."
    
    Return the result of calling `birthday()` for a dog "Bob" who is 4 years old.
    """
    # TODO: Write your code here
    class Dog():
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def bark(self, times):
            return ("Woof! " * times)+(self.name)

        def birthday(self):
            self.age += 1
            return f"Happy birthday {self.name}! You are now {self.age} years old."

    dog1 = Dog("Bob", 4)
    return dog1.birthday()

# ----------------------
# Helper runner for testing
# ----------------------

def _run_and_print(fn, label):
    try:
        result = fn()
        print(f"{label}: {result}")
    except NotImplementedError:
        print(f"{label}: (not implemented)")


def main():
    print("Running Lab 6 - Classes exercises...\n")
    for i in range(1, 11):
        _run_and_print(globals()[f"ex_1_{i}"], f"1.{i}")


if __name__ == "__main__":
    main()