"""
Decorators in Python!

A decorator in Python is a function that takes another function as its argument, and returns yet another function.
Decorators can be extremely useful as they allow the extension of an existing function,
without any modification to the original function source code.


Source:
https://towardsdatascience.com/how-to-use-decorators-in-python-by-example-b398328163b
https://www.youtube.com/watch?v=P0aW1czXHio
"""
import time


def decorator_func(func):

    def wrapper():  # All decorators need to have a function inside them
        # All these lines will be "added" to the primary function
        start_time = time.time()
        func()  # This is the primary function running

        # This lines will be "added" too
        end_time = time.time()
        result = (end_time - start_time) * 1000
        print(f'The primary function takes {result} seconds')
    return wrapper  # All decorators need to return a function


@decorator_func  # In this line will decorate the function
def say_hello():
    for x in range(100):
        print('Hello user!')


say_hello()
