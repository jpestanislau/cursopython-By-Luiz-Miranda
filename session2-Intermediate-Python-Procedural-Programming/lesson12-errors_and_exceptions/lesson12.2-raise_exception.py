"""
Raise an exceptions in Python!

Use the "raise" keyword to throw (or raise) an exception.


Source:
https://www.w3schools.com/python/gloss_python_raise.asp
https://docs.python.org/3/tutorial/errors.html#raising-exceptions
"""


def divide(n1, n2):
    try:
        return n1/n2
    except ZeroDivisionError as error:
        print(error)
        raise  # This line RAISES the error so that it can also be handled and by who called the function


def access_index(l, index):
    if index > len(l):
        raise IndexError('The index is out of bounds')  # We can raise your own exception
    return l[index]


try:
    print(divide(10, 0))

except ZeroDivisionError as error:
    print('I am with the error too! It is:', error)

try:
    x = [0, 2]
    access_index(x, 3)

except IndexError as error:
    print(error)
