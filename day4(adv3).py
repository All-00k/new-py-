# #Polymorphism
#     #Duck typing
#
# class Duck:
#     def quack(self):
#         print("Quack")
#
# class Person:
#     def quack(self):
#         print("I'm quacking like a duck!")
#
# duck = Duck()
# person = Person()
#
# duck.quack()
# person.quack()
from PIL.ImageFile import StubImageFile


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# class Bird:
#     def fly(self):
#         print("fly with wings")
#
# class Airplane:
#     def fly(self):
#         print("fly with fuel")
#
# class Fish:
#
#     def swim(self):
#         print("fish swim in sea")
#
# for obj in Bird(), Airplane(), Fish():
#     obj.fly() #attribution error because fish do not have a fly attribute

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#method overloading

# class MYclass:
#     def sum(self, a = None , b =None, c = None):
#         s =0
#         if a != None and  b!=None and c != None:
#             s = a + b + c
#         elif a != None and b != None:
#             s = a + b
#         else:
#             s = a
#         return s
#
# s = MYclass()
# print(s.sum(1))
# print(s.sum(2,5))
# print(s.sum(2,5,2))

#!!!!~!!!!!!!!!!!!!~!@~!~!!~!!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!!~!~!


#operator overloading

# class Student:
#     def __init__(self,m1,m2):
#         self.m1 = m1
#         self.m2 = m2
#
#     #overloading the + operator
#     def __add__(self,other):
#         m1 = self.m1 + other.m1
#         m2 = self.m2 + other.m2
#         s3 = Student(m1,m2)
#         return s3
# s1 = Student(58, 59)
# s2 = Student(68, 65)
# s3 = s1+s2
# print(s3.m1)


#
# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)
#
#     def __sub__(self, other):
#         return Vector(self.x - other.x, self.y - other.y)
#
#     def __mul__(self, other):
#             return self.x * other.x + self.y * other.y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
# v1 = Vector(2,3)
# v2 = Vector(4,5)
#
# v3 = v1 + v2
# v4 = v1 - v2
# dot_product = v1 * v2
#
# print("v1:", v1)
# print("v2:", v2)
# print("v1 + v2", v3)
# print("v1 - v2", v4)
# print("v1 * v2 (dot_product):", v1* v2)

#!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!


#Method over riding
#
# class Animal:
#     def speak(self):
#         print("The animal makes a sound")
#
# class Dog(Animal):
#     def speak(self):
#         print("The dog Barks")
#
# class Cat(Animal):
#         print("The cat meows")
#
# animal = Animal()
# dog = Dog()
# cat = Cat()
#
# animal.speak()
# dog.speak()
# cat.speak()


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# class BankAccount:
#     def __init__(self,account_number, balance):
#         self.account_number = account_number
#         self.balance = balance
#
#     def calculate_interest(self):
#         return self.balance * 0.01 # default interest rate 1%
#
#     def display(self):
#         print(f"Account number: {self.account_number}", f"Balance: {self.balance}")
#
# class Savings_Account(BankAccount):
#     def calculate_interest(self):
#         return self.balance * 0.04 #4% interest
#
# class CurrentAccount(BankAccount):
#     def calculate_interest(self):
#         return self.balance * 0.02 #2% interest
#
#
# savings = Savings_Account("5123", 1000)
# current = CurrentAccount("C456", 2000)
# savings.display()
# current.display()
#
# print(f"Savings Account Interest: {savings.calculate_interest()}")
# print(f"Current Account Interest: {current.calculate_interest()}")


##~#~#~#~#~##~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~
#Abstract class
#
# from abc import ABC, abstractmethod
# class computer(ABC):
#     @abstractmethod
#     def process(self):
#         pass
#     def message(self):
#         print("Computer is an electronic device")
#
# class Laptop(computer):
#     def process(self):
#         print("Executing Laptop Processes")
#
# class Desktop(computer):
#     def process(self):
#         print("Executing Desktop Processes")
#
# com1 = Laptop()
# com2 = Desktop()
# com1.process()
# com2.message()
# com2.process()



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
#     @abstractmethod
#     def perimeter(self):
#         pass
#
# # Concrete method
#     def description(self):
#         return "This is a shape."
#
# # Concrete Class: Circle
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius * self.radius
#
#     def perimeter(self):
#         return 2 * 3.14 * self.radius
#
# # Concrete Class: Rectangle
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return self.length * self.width
#
#     def perimeter(self):
#         return 2 * (self.length + self.width)
#
# # Example usage
# circle = Circle(5)
# rectangle = Rectangle(4, 6)
#
# print(f"Circle area: {circle.area()}")
# print(f"Circle perimeter: {circle.perimeter()}")
# print(f"Circle description: {circle.description()}")
#
# print(f"Rectangle area: {rectangle.area()}")
# print(f"Rectangle perimeter: {rectangle.perimeter()}")
# print(f"Rectangle description: {rectangle.description()}")

#

















