# def generate_numbers():
#     for num in range(1, 11):
#         yield num
#
# numbers_generator = generate_numbers()
# print(type(numbers_generator))
#
# for number in numbers_generator:
#     print(number)

#!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) +1):
#         if num % i == 0:
#             return False
#     return True
# def generate_prime(start, end):
#     for num in range(start, end + 1):
#         if is_prime(num):
#             yield num
#
# prime_generator = generate_prime(5, 50)
#
# for prime in prime_generator:
#     print(prime , end = ', ')



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# yield in generator
# def rev_str(my_str):
#     length = len(my_str)
#     for i in range(length -1, -1, -1):
#         yield my_str[i]
#
# for char in rev_str("hello"):
#     print(char)


# #multiple generator
# def my_gen(x):
#     while(x>0):
#         if x% 2==0:
#             yield 'Even'
#         else:
#             yield 'Odd'
#         x -= 1
# for i in my_gen(7):
#     print(i)
#

#````````````~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Coroutine

