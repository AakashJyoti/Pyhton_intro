# Question 1: Basic Class and Object
# Summary: Create a Car class with attributes like brand and model. Then create an instance of this class.


# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model


# Astr_car = Car("Toyota", "Supra-Mk4")

# print(Astr_car.brand)
# print(Astr_car.model)

#################################################


# Question 2: Class Method and Self
# Summary: Add a method to the Car class that displays the full name of the car (brand and model).


# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def full_name(self):
#         return f"{self.brand} {self.model}"


# Astr_car = Car("Toyota", "Supra-Mk4")

# print(Astr_car.full_name())

#################################################


# Question 3: Inheritance
# Summary: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.


# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def full_name(self):
#         return f"{self.brand} {self.model}"


# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size


# my_tesla = ElectricCar("Tesla", "Model S", "85kwh")
# print(my_tesla.model)
# print(my_tesla.full_name())

#################################################


# Question 4: Encapsulation
# Summary: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.


# class Car:
#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.__model = model

#     def set_model(self, model):
#         self.__model = model

#     def get_brand(self):
#         return self.__brand + "!..."

#     def full_name(self):
#         return f"{self.__brand} {self.__model}"


# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size


# my_tesla = ElectricCar("Tesla", "Model S", "85kwh")
# my_tesla.set_model("Model Z")
# print(my_tesla.get_brand())
# print(my_tesla.full_name())

#################################################


# Question 5: Polymorphism
# Summary: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.


# class Car:
#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.__model = model

#     def set_model(self, model):
#         self.__model = model

#     def get_brand(self):
#         return self.__brand + "!..."

#     def full_name(self):
#         return f"{self.__brand} {self.__model}"

#     def fuel_type(self):
#         return "Petrol and Diesel"


# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size

#     def fuel_type(self):
#         return "Electric charge"


# my_tesla = ElectricCar("Tesla", "Model S", "85kwh")
# my_supra = Car("Toyota", "Supra")

# print("my_supra", my_supra.fuel_type())
# print("my_tesla", my_tesla.fuel_type())

#################################################


# Question 6: Class Variables
# Summary: Add a class variable to Car that keeps track of the number of cars created.


# class Car:
#     total_car = 0

#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.__model = model
#         Car.total_car += 1

#     def set_model(self, model):
#         self.__model = model

#     def get_brand(self):
#         return self.__brand + "!..."

#     def full_name(self):
#         return f"{self.__brand} {self.__model}"

#     def fuel_type(self):
#         return "Petrol and Diesel"


# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size

#     def fuel_type(self):
#         return "Electric charge"


# ElectricCar("Tesla", "Model S", "85kwh")
# Car("Toyota", "Supra")

# print(Car.total_car)

#################################################


# Question 7: Static Method
# Summary: Add a static method to the Car class that returns a general description of a car.


# class Car:
#     total_car = 0

#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.__model = model
#         Car.total_car += 1

#     def set_model(self, model):
#         self.__model = model

#     def get_brand(self):
#         return self.__brand + "!..."

#     def full_name(self):
#         return f"{self.__brand} {self.__model}"

#     def fuel_type(self):
#         return "Petrol and Diesel"

#     @staticmethod # decorators
#     def general_desc():
#         return "Cars are means of transport"


# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size

#     def fuel_type(self):
#         return "Electric charge"


# ElectricCar("Tesla", "Model S", "85kwh")
# Car("Toyota", "Supra")

# print(Car.general_desc())

#################################################


# Question 8: Property Decorators
# Summary: Use a property decorator in the Car class to make the model attribute read-only.


# class Car:
#     total_car = 0

#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.__model = model
#         Car.total_car += 1

#     def set_model(self, model):
#         self.__model = model

#     def get_brand(self):
#         return self.__brand + "!..."

#     def full_name(self):
#         return f"{self.__brand} {self.__model}"

#     def fuel_type(self):
#         return "Petrol and Diesel"

#     @staticmethod  # decorators
#     def general_desc():
#         return "Cars are means of transport"

#     @property
#     def model(self):
#         return self.__model


# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size

#     def fuel_type(self):
#         return "Electric charge"


# my_tesla = ElectricCar("Tesla", "Model S", "85kwh")
# Car("Toyota", "Supra")

# # my_tesla.model = "City" // not work

# print(my_tesla.model)
# print(my_tesla.model())

#################################################


# Question 9: Class Inheritance and isinstance() Function
# Summary: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.


# class Car:
#     total_car = 0

#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.__model = model
#         Car.total_car += 1

#     def set_model(self, model):
#         self.__model = model

#     def get_brand(self):
#         return self.__brand + "!..."

#     def full_name(self):
#         return f"{self.__brand} {self.__model}"

#     def fuel_type(self):
#         return "Petrol and Diesel"

#     @staticmethod  # decorators
#     def general_desc():
#         return "Cars are means of transport"

#     @property
#     def model(self):
#         return self.__model


# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size

#     def fuel_type(self):
#         return "Electric charge"


# my_tesla = ElectricCar("Tesla", "Model S", "85kwh")

# print("Is Car instance", isinstance(my_tesla, Car))
# print("Is Electric instance", isinstance(my_tesla, ElectricCar))

#################################################


# Question 10: Multiple Inheritance
# Summary: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.


# class Car:
#     total_car = 0

#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.__model = model
#         Car.total_car += 1

#     def set_model(self, model):
#         self.__model = model

#     def get_brand(self):
#         return self.__brand + "!..."

#     def full_name(self):
#         return f"{self.__brand} {self.__model}"

#     def fuel_type(self):
#         return "Petrol and Diesel"

#     @staticmethod  # decorators
#     def general_desc():
#         return "Cars are means of transport"

#     @property
#     def model(self):
#         return self.__model


# class Battery:
#     def battery_info(self):
#         return "this is battery"


# class Engine:
#     def engine_info(self):
#         return "this is engine"


# class ElectricCar2(Battery, Engine, Car):
#     pass


# my_new_tesla = ElectricCar2("Tesla", "Model X")

# print(my_new_tesla.battery_info())
# print(my_new_tesla.engine_info())
