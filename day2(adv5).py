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

class MathsOperations:
    @staticmethod
    def add_num(a,b):
        return a+b
    @staticmethod
    def sub(a,b):
        return a-b

obj = MathsOperations()
result_add = MathsOperations.add_num(10,20) # call by className
result_sub = obj.sub(10,20) #call by objectName

print(f"Addition: {result_add}")
print(f"Subtraction: {result_sub}")




