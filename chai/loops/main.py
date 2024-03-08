# Question 1 : Counting Positive Numbers
# Summary : Given a list of numbers, count how many are positive.

# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

# positive_count = 0

# for superman in numbers:
#     if superman > 0:
#         positive_count += 1

# print(positive_count)

###################################################################


# Question 2 : Sum of Even Numbers
# Summary : Calculate the sum of even numbers up to a given number n.

# n = 10
# even_sum = 0

# for i in range(1, n + 1):
#     if i % 2 == 0:
#         even_sum += i

# print("even_sum", even_sum)

#######################################################################


# Question 3 : Multiplication Table Printer
# Summary : Print the multiplication table for a given number up to 10, but skip the fifth iteration.

# given_number = 5

# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(given_number, " * ", i, " = ", given_number * i)

#############################################################################


# Question 4 : Reverse a String
# Summary : Reverse a string using a loop.

# input_str = "Astr"
# rev_str = ""

# for char in input_str:
#     rev_str = char + rev_str

# print(rev_str)

##################################################################


# Question 5 :  Find the First Non-Repeated Character
# Summary :  Given a string, find the first non-repeated character.

# str = "aakash"

# for char in str:
#     if str.count(char) == 1:
#         print("first non-repeated character is: ", char)
#         break

##########################################################################


# Question 6 : Factorial Calculator
# Summary :  Compute the factorial of a number using a while loop.

# number = 12
# factorial = 1

# while number > 0:
#     factorial *= number
#     number -= 1

# print({factorial})

############################################################################


# Question 7 : Validate Input
# Summary : Keep asking the user for input until they enter a number between 1 and 10.

# while True:
#     user_num = int(input("Enter num bw 1 - 10: "))
#     if 1 <= user_num <= 10:
#         print("User valid input: ", user_num)
#         break
#     else:
#         print("Invalid number")

#########################################################################


# Question 8 : Prime Number Checker
# Summary : Check if a number is prime.

# num = 23
# is_Prime = True

# if num > 1:
#     for i in range(2, num):
#         if num % i == 0:
#             is_Prime = False
#             break

# print("IsPrime: ", is_Prime)

####################################################################


# Question 9 : List Uniqueness Checker
# Summary : Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

# items = ["apple", "banana", "orange", "apple", "mango"]
# unique_item = set()

# for item in items:
#     if item in unique_item:
#         print("dub item: ", item)
#         break
#     unique_item.add(item)

##################################################################


# Question 10 : Exponential Backoff
# Summary : Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

# import time

# wait_time = 1
# max_retries = 5
# attempts = 0

# while attempts < max_retries:
#     time.sleep(wait_time)
#     print("wait_time", wait_time)
#     print("attempts", attempts)
#     wait_time *= 2
#     attempts += 1
