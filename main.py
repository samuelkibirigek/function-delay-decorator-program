# This program demonstrates how decorators are created and work in python.

import time


def delay_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        time_spent = end_time - start_time
        print(f"{function.__name__} run time: {time_spent}")
    return wrapper_function


@delay_decorator
def fast_function():
    for i in range(10000000):
        calculation = i * i


@delay_decorator
def slow_function():
    for i in range(100000000):
        calculation_two = i * i


fast_function()
slow_function()