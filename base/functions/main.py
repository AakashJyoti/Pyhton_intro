# Question 1 :  Basic Function Syntax
# Summary : Write a function to calculate and return the square of a number.


# def square(num):
#     return num**2


# print(square(9))

########################################################

# Question 2 : Function with Multiple Parameters
# Summary : Create a function that takes two numbers as parameters and returns their sum.


# def sum(num_1, num_2):
#     return num_1 + num_2


# print(sum(9, 4))

#######################################################

# Question 3 : Polymorphism in Functions --> ek chiz anek kaam
# Summary : Write a function multiply that multiplies two numbers, but can also accept and multiply strings.


# def multiply(p1, p2):
#     return p1 * p2


# print(multiply(2, 5))
# print(multiply("h", 5))
# print(multiply(5, "h"))

########################################################


# Question 4 : Function Returning Multiple Values
# Summary : Create a function that returns both the area and circumference of a circle given its radius.

# import math


# def calculate(radius):
#     area = round(math.pi * radius**2, 2)
#     circumference = round(2 * math.pi * radius, 2)
#     return {"area": area, "circumference": circumference}


# print(calculate(5))

#########################################################


# Question 5 : Default Parameter Value
# Summary : Write a function that greets a user. If no name is provided, it should greet with a default name.


# def greet(name="Admin"):
#     return "Hello " + name + " !"


# print(greet("Astr"))
# print(greet())

############################################################


# Question 6 : Lambda Function
# Summary : Create a lambda function to compute the cube of a number.


# cube = lambda x: x**2

# print(cube(3))

#############################################################


# Question 7 : Function with *args
# Summary : Write a function that takes variable number of arguments and returns their sum.


# def sum_all(*args):
#     return sum(args)


# print(sum_all(1, 2))
# print(sum_all(1, 2, 3))
# print(sum_all(1, 2, 3, 4, 5))

##################################################################


# Question 8 : Function with **kwargs
# Summary : Create a function that accepts any number of keyword arguments and prints them in the format key: value.


# def print_kwargs(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")


# print_kwargs(power="Backchodi", name="Jabba")

##################################################################


# Question 9 : Generator Function with yield
# Summary :  Write a generator function that yields even numbers up to a specified limit.


# def even_generator(limit):
#     for i in range(2, limit + 1, 2):
#         yield i


# for num in even_generator(20):
#     print(num)

# for num in even_generator(20):
#     print("he", num)

##################################################################


# Question 10 : Recursive Function
# Summary : Create a recursive function to calculate the factorial of a number.


# def find_factorial(num):
#     if num == 0:
#         return 1
#     return num * find_factorial(num - 1)


# print(find_factorial(5))
