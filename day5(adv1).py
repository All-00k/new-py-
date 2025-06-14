# def outerfunction(text):
#     text = text
#     def innerfunction():
#         print(text)
#     return innerfunction
#
# myFunction = outerfunction("hello")
# myFunction()




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Decorators

#
# def decor(addition):
#     def inner():
#         result = addition() # existing
#         num3 =  float(input("Enter the number 3: "))
#         result  =  result + num3
#         return result
#     return inner
#
#
# @decor
# def addition():
#     num1 = float(input("Enter number 1: "))
#     num2 = float(input("Enter number 2: "))
#     result = num1 + num2
#     return result
#
# # addition = decor(addition())
# print("Addition is: ",addition())




#!~!~!~!~!~!~!~!~!~!~!~!~!~!~!!~!~!~!~!~!~!
# def decor(func):
#     def inner():
#         print("___________________")
#         func()
#         print("___________________")
#     return inner
# @decor()
# def msg():
#     print("Python Programming")
#
# # msg = decor(msg)  we use decorator dispite og using this
# msg()

#!~!~!~!~~~~~~~~~~~~~~~!~!~!~!!!!!!!!!!!!!!!!!!!!!!!!!~!~!~1`1`1`1


# from datetime import datetime
#
# def not_during_night(func):
#     def inner():
#         if 7 <= datetime.now().hour < 22:
#             func()
#         else:
#             print("Playing BureDin...sojao gn")
#     return inner
#
# @not_during_night
# def music():
#     print("Playing Namastute...moshpit")
#
# music()




#~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!

# def do_twice(func):
#     def wrapper_do_twice(*args, **kargs):
#         func(*args, **kargs)
#         func(*args, **kargs)
#     return wrapper_do_twice
#
# @do_twice
# def message(name):
#     print(f"Hello {name}")
#
# message("Mohit")

#~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!

