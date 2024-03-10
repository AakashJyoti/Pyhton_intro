# Question 1 : Age group Categorization
# Summary : Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

# age = 26
# if age < 13:
#     print("Child")
# elif age < 20:
#     print("Teenage")
# elif age < 60:
#     print("Adult")
# else:
#     print("Senior")

###############################################################


# Question 2 : Movie Ticket Pricing
# Summary : Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

# age = 26
# day = "Wednesday"
# price = 8 if age < 18 else 12

# if day == "Wednesday":
#     price = price - 2

# print("Ticket cost:", price)

#####################################################################


# Question 3 : Grade Calculator
# Summary : Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

# marks = -102

# if marks > 101 or marks < 0:
#     print("Invalid Marks")
#     exit()

# if marks >= 90:
#     grade = "A"
# elif marks >= 80:
#     grade = "B"
# elif marks >= 70:
#     grade = "C"
# elif marks >= 60:
#     grade = "D"
# else:
#     grade = "F"
# print("Grade: ", grade)

###########################################################


# Question 4 : Fruit Ripeness Checker
# Summary : Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

# fruit = "Banana"
# color = "Brown"

# if fruit == "Banana":
#     if color == "Green":
#         print("Unripe")
#     elif color == "Yellow":
#         print("Ripe")
#     elif color == "Brown":
#         print("Overripe")
#     else:
#         print("Unknown color")
# else:
#     print("unknown fruit")

##############################################################


# Question 5 : Weather Activity Suggestion
# Summary : Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

# weather = "Rainy"

# if weather == "Sunny":
#     activity = "Go for a walk"
# elif weather == "Rainy":
#     activity = "Read a book"
# elif weather == "Snowy":
#     activity = "Build a snowman"
# else:
#     activity = "Good day to Die"

# print(activity)

#################################################################


# Question 6 : Transportation Mode Selection
# Summary : Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

# distance = 15

# if distance < 3:
#     transport = "Walk"
# elif distance <= 15:
#     transport = "Bike"
# else:
#     transport = "Car"

# print(transport)

##########################################################


# Question 7 : Coffee Customization
# Summary : Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

# order_size = "Small"
# extra_shot = True

# if extra_shot:
#     coffee = order_size + " coffee with extra shot"
# else:
#     coffee = order_size + " coffee"

# print(coffee)

##############################################################


# Question 8 : Password Strength Checker
# Summary : Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong)

# password = "Aakash@1"

# password_length = len(password)
# if password_length < 6:
#     status = "Week"
# elif password_length <= 10:
#     status = "Medium"
# else:
#     status = "Strong"

# print(status)

##########################################################


# Question 9 : Leap Year Checker
# Summary : Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

# year = 2023
# is_leap_year = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# if is_leap_year:
#     print("Year is a Leap Year")
# else:
#     print("Year is not a Leap Year")

##############################################################


# Question 10 : Pet Food Recommendation
# Summary : Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

# species = "lion"
# age = 5

# if species == "dog":
#     if age < 2:
#         food = "Puppy food"
#     else:
#         food = "Senior dog food"
# elif species == "cat":
#     if age < 5:
#         food = "kitten food"
#     else:
#         food = "Senior cat food"
# else:
#     food = "Data not available"

# print(food)
