# import math
# from distutils.command.install import value
#
#
# class Fraction:
#     def __init__(self, numerator, denominator):
#         self.numerator = numerator
#         self.denominator = denominator
#
#     def simplify(self):
#         common_divisor = math.gcd(self.numerator, self.denominator)
#         self.numerator //= common_divisor
#         self.denominator //= common_divisor
#
#     def __add__(self, other):
#         new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
#         new_denominator = self.denominator * other.denominator
#         return Fraction(new_numerator, new_denominator)
#
#     def __eq__(self, other):
#         return self.numerator == other.numerator and self.denominator == other.denominator
#
#     def __lt__(self, other):
#         return self.numerator * other.denominator < other.numerator * self.denominator
#
#     def __repr__(self):
#         return f"{self.numerator}/{self.denominator}"
#
# f1 = Fraction(1, 2)
# f2 = Fraction(2, 3)
#
# f3 = f1 + f2
# print(f3)
#
# print(f1==f2)
# print(f1 < f2)








#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# class MyClass:
#     def __init__(self,value):
#         self.value = value
#
# def print_value(ogj):
#     print(f"The value is: {obj.value}")
#
# obj = MyClass(10)
# print_value(obj)
#


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#
# class Person:
#     def __init__(self,name):
#         self.name = name
#     def __repr__(self):
#         return f"Person({self.name})"
#
# class Greeting:
#     def generate_greeting(self, person):
#         return f"Hello, {person.name}! Welcome!"
#
# person = Person("Alice")
# greeting = Greeting()
#
# message = greeting.generate_greeting(person)
# print(message)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




# class MyClass:
#     def __init__(self,value):
#         self.value = value
#
# def create_object(value):
#     return MyClass(value)
#
# obj = create_object(10)
# print(obj.value)







#`~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#question rectangle

# class Rectangle:
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width*self.height
#     def combine(self,other):
#         new_width = self.width
#         new_area = other.width*other.height
#         new_height = new_area/new_width
#         return Rectangle(new_width, new_height)
#
#     def __repr__(self):
#         return f"Rectangle({self.width}, {self.height})"
# rect1 = Rectangle(10,20)
# rect2 = Rectangle(10,12)
# combine_rect = rect1.combine(rect2)
# print(combine_rect)




