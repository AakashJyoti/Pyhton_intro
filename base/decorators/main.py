# Question 1 : Timing Function Execution
# Summary : Write a decorator that measures the time a function takes to execute.

import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end - start} time")
        return result

    return wrapper


@timer
def example_func(n):
    time.sleep(n)


# example_func(2)

###############################################################


# Question 2 : Debugging Function Calls
# Summary : Create a decorator to print the function name and the values of its arguments every time the function is called.


def debugger(func):
    def wrapper(*args, **kwargs):
        args_value = ", ".join(str(arg) for arg in args)
        kwargs_values = ", ".join(f"{key}={value}" for key, value in kwargs.items())
        print(
            f"Function name: {func.__name__} with args: {args_value} with kwargs: {kwargs_values}"
        )
        return func(*args, **kwargs)

    return wrapper


@debugger
def greet(name, greeting="Hello"):
    print(f"{name} {greeting}!..")


# greet("Astr", "Kaha hai beee")

###############################################################


# Question 3 : Cache Return Values
# Summary : Implement a decorator that caches the return values of a function, so that when it's called with the same arguments, the cached value is returned instead of re-executing the function.


def cache(func):
    cache_value = {}
    func_name = func.__name__

    def wrapper(*args, **kwargs):
        if (func_name, args) in cache_value:
            return cache_value[func_name, args]
        result = func(*args, **kwargs)
        cache_value[func_name, args] = result
        return result

    return wrapper


@cache
def long_running_func(a, b):
    time.sleep(4)
    return a + b


@cache
def long_running_func_returns(a, b):
    time.sleep(4)
    return a + b


# print(long_running_func(2, 3))
# print(long_running_func(2, 3))

# print(long_running_func_returns(5, 6))
# print(long_running_func_returns(5, 6))
