"""
1 - Create a function1 that takes a function2 as a parameter and returns the value of the executed function2.
"""


def func1(other_func):
    other_func()


def func2():
    print('I am using Python!')


# func1(func2)

"""
2 - Create a function1 that takes a function2 as a parameter and returns the value of the executed function2. Make 
function1 execute two functions that take a different number of arguments. 
"""


def func3(other_func, *args, **kwargs):
    return other_func(*args, **kwargs)


def func4(name):
    return f'I am using Python, {name}!'


def func5(name, hour):
    return f'I am using Python for {hour} hours, {name}!'


print(func3(func4, 'Fulano'))
print(func3(func5, 'Fulano', 23))
