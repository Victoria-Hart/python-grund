from abc import ABC, abstractmethod

class Person:
    name = 'John'

person1 = Person()
person2 = Person()
print(person1.name)

class Car:
    wheels = 4

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

car1 = Car('Volvo', 'Red')
print(car1.brand)
print(car1.color)
print(car1.wheels)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def book_info(self):
        print(f'{self.title} by: {self.author}')

book1 = Book('Python 101', 'John Doe')
book1.book_info()
print(book1)

class Song:
    def __init__(self, title, writer):
        self.title = title
        self.writer = writer

    def __str__(self):
        return f'Title: {self.title}\nWriter: {self.writer}' 
    
song1 = Song('I love python', 'Jane Doe')
print(song1)

class Phone:
    category = 'Electronics'

    def __init__(self, brand, price):
        self.brand = brand 
        self.price = price

phone1 = Phone('Apple', 15000)
phone2 = Phone('Samsung', 14000)

print(phone1.category)
print(phone1.price)

phone1.price = 12000
print(phone1.price)

Phone.category = 'Gadgets'
print(phone1.category)
print(phone2.category)

class Dog:
    def __init__(self, name, age):
        self._name = name
        self._age = age 

    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, value):
        self._name = value
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 0:
            print('Age cannot be negative value')
        else: 
            self._age = value

dog1 = Dog('John', 10)
dog1.name = 'Jane'
dog1.age = -3
print(dog1.name, dog1.age)

class Animal:
    def sound(self):
        print('Sound not defined')

class Cow(Animal):
    def sound(self):
        print('MO')

cow = Cow()
cow.sound()

class Vehicle(ABC):
    @classmethod
    @abstractmethod
    def vehicle_type(cls):
        pass

    def fuel_type(self):
        return 'Generic fuel'
    
class Car(Vehicle):
    @classmethod
    def vehicle_type(cls):
        return 'Car'
    
class Boat(Vehicle):
    @classmethod
    def vehicle_type(cls):
        return 'Boat'
    
car = Car()
print(car.fuel_type())
print(car.vehicle_type())

class Electronic:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f'Electronic name: {self.name}')

class Phone(Electronic):
    def make_call(self):
        print(f'{self.name} makes a call')

class Smartphone(Phone):
    def browse_internet(self):
        print(f'{self.name} browsing internet')

class WifiEnabled:
    def connect_wifi(self):
        print('Connected to wifi')

class Laptop(Electronic, WifiEnabled):
    def code(self):
        print(f'{self.name} is coding')

laptop = Laptop('MacBook')
laptop.display_name()
laptop.connect_wifi()
laptop.code()




    





        

