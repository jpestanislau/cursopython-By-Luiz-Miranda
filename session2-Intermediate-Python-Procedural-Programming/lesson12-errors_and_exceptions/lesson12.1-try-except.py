"""
Try and Except in Python!

The TRY block lets you test a block of code for errors.
The EXCEPT block lets you handle the error.
The ELSE block lets you execute code when THERE IS NO ERROR.
The FINALLY block lets you execute code, regardless of the result of the try- and except blocks.

Source:
https://www.w3schools.com/python/python_try_except.asp
https://docs.python.org/3/tutorial/errors.html#handling-exceptions
"""
try:
    print(a)
    a = 1 / 0

    b = []
    print(b[1])
except NameError as error:
    print('Name Error occurred!')

except ZeroDivisionError as error:
    print('YOU TRUED DIVIDE BY ZERO!')

except (IndexError, KeyError) as error:
    print('Index or Key error occurred!')

except Exception as error:
    # Exception is mother of all errors
    print('A generic error occurred')

else:
    print('This block will execute if the try ends without error')

finally:
    print('This block will execute anyway')

print('The code go won!')
