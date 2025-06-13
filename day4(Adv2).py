# class Animal:
#     # attribute and method of the parent class
#     name = ""
#
#     def eat(self):
#         print("I can eat")
#
# # inherit from animal
# class Dog(Animal):
#
#     #new method in subclass
#     def display(self):
#         #access naem attribute of superclass using self\
#         print(f"My name is {self.name}..............bhow bhow")
#
# # create an object of the subclass
# labrador = Dog()
#
# #access superclass attribure and method
# labrador.name = "Euro"
# labrador.eat()
#
# # call subclas method
# labrador.display()




 # ``~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 #
 #
 # class Father:
 #     money = 1000
 #     def show(self):
 #         print("Parent class instance method")
 #    @classmethod
 #    def moneyshow(clas):
 #        print("Parent class class method : TOtal money = ", clas.money)
 #
 #    @staticmethod
 #    def stat_method():
 #        a =5
 #        print("Parent class Static method: the value of a is",a)
 #
 #    class Son(Father):
 #        def son_display(self):
 #            print("Parent class Father class method : son_display()")
 #





#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#
#
# class Father:
#     def __init__(self):
#         self.money = 2000
#         print("Father Class Constructor")
#
# class Son(Father):
#     def __init__(self):
#         self.money = 5000
#         print("Son Class Constructor")
#
#     def dispaly(self):
#         print(self.money)
#
# s = Son()
# s.dispaly()



#`~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# class Person:
#     def __init__(self,fname, lname):
#         self.fname = fname
#         self.lname = lname
#         print("First name is {} and last name is {}".format(self.fname, self.lname))
#
# class Student(Person):
#     def __init__(self,fname,lname):
#         super().__init__(fname,lname)
#         print("Inside Student class init")
#
# s = Student("Ananya","Shukla")




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#
# class Father:
#     def __init__(self):
#         print("Father class constructor")
#     def show_father(self):
#         print("Father class method")
#
# class Son(Father):
#     def __init__(self):
#         print("Son class constructor")
#     def show_son(self):
#         print("Son class method")
#
# class Grandson(Son):
#     def _init__(self):
#         print("Grandson class constructor")
#     def show_grandson(self):
#         print("Grandson class method")
#
# g = Grandson()
# g.show_grandson()
# g.show_son()
# g.show_father()


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




#private variable

# class Computer:
#     def __init__(self):
#         self.__maxprice = 900
#     def sell(self):
#         print("SElling Price: {}".format(self.__maxprice))
#     def setMaxPrice(self, price):
#         self.__maxprice = price
# c = Computer()
# c.sell()
# c.setMaxPrice(1000)
# c.sell()




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# class Student:
#     _name = None
#     _roll = None
#     _branch = None
#
#     def __init__(self, name, roll, branch):
#         self._name = name
#         self._roll = roll
#         self._branch = branch
#
#     def _displayinfo(self):
#         print("Roll: ", self._roll)
#         print("Branch: ", self._branch)
#
# class Learnowx(Student):
#         def __init__(self, name, roll, branch):
#             Student.__init__(self, name, roll, branch)
#
#         def _displayDetails(self):
#             print("Name: ", self._name)
#             self._displayinfo()
#
# obj = Learnowx("Alok", 102200, "Data Science")
# obj._displayDetails()
#


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# class Student:
#     __name = None
#     __roll = None
#     __branch = None
#
#     def __init__(self, name, roll, branch):
#         self.__name = name
#         self.__roll = roll
#         self.__branch = branch
#     def __displayinfo(self):
#         print("Name: ", self.__name)
#         print("Roll: ", self.__roll)
#         print("Branch: ", self.__branch)
#     def accessPrivateMethod(self):
#         self.__displayinfo()
#
# obj = Student("Ananya", 1261698, "Data Science")
# obj.accessPrivateMethod()
#


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
