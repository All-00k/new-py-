# use of decorator
# class Student:
#     counter = 0
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         Student.counter += 1
#     def msg(self):
#         print("Hello"+self.name+"you got",self.marks,"% marks")
#     @classmethod #function decorator
#     def object_count(cls):
#         return cls.counter
# s1 = Student("Alok",66)
# s2 = Student("abc",32)
# print(Student.object_count())
# print(s1.object_count())

#```````````````````````````````````````````````````````````````````````````````

# class MathsOperations:
#     @staticmethod
#     def add_num(a,b):
#         return a+b
#     @staticmethod
#     def sub(a,b):
#         return a-b
#
# obj = MathsOperations()
# result_add = MathsOperations.add_num(10,20) # call by className
# result_sub = obj.sub(10,20) #call by objectName
#
# print(f"Addition: {result_add}")
# print(f"Subtraction: {result_sub}")


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# class Student:
#     def __init__(self):
#         print("Default constructor called")
#
#     def __init__(self, name, marks, age):
#         self.name = name
#         self.marks = marks
#         self.age = age
#         print("Parameterized constructor called")
#     def show_info(self ):
#         print("Name", self.name)
#         print("Marks", self.marks)
#         print("Age", self.age)
#     def __del__(self):
#         print("Destructors called")
#
#
# s1 = Student() #default parameter is being called
# s2 = Student("Rohit", 95.5, 19)
# s1.show_info()
# s2.show_info()
#





#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~









